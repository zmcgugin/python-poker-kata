import unittest
from poker.poker_winner import PokerWinner


class MyTest(unittest.TestCase):

    def test_high_card_1(self):
        zaks_hand = ('Zak', ['AS', '2H', '3H', 'JC', '8D'])
        jons_hand = ('Jon', ['KS', '2H', '3H', 'JC', '8D'])
        self.assertEqual(PokerWinner.find_winning_hand([zaks_hand, jons_hand]), 'Zak')

    def test_high_card_2(self):
        zaks_hand = ('Zak', ['KS', '2H', '3H', 'JC', '8D'])
        jons_hand = ('Jon', ['6S', '2H', '3H', 'JC', 'AS'])
        self.assertEqual(PokerWinner.find_winning_hand([zaks_hand, jons_hand]), 'Jon')
