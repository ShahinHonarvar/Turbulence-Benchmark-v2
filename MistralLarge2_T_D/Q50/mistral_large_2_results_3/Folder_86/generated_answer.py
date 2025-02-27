from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(words):

    def is_anagram(word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())
    anagram_count = 0
    checked_pairs = set()
    for word1, word2 in combinations(words, 2):
        if len(word1) >= 3 and len(word2) >= 3:
            sorted_word1 = tuple(sorted(word1.lower()))
            sorted_word2 = tuple(sorted(word2.lower()))
            if sorted_word1 == sorted_word2:
                pair = tuple(sorted([word1, word2]))
                if pair not in checked_pairs:
                    anagram_count += 1
                    checked_pairs.add(pair)
    return anagram_count >= 115