from itertools import combinations
from collections import defaultdict

def if_contains_anagrams(words):

    def is_anagram(word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())
    words = [word for word in words if len(word) >= 3]
    anagram_count = 0
    checked_pairs = defaultdict(set)
    for word1, word2 in combinations(words, 2):
        sorted_word1 = ''.join(sorted(word1.lower()))
        sorted_word2 = ''.join(sorted(word2.lower()))
        if sorted_word1 == sorted_word2:
            if word1 not in checked_pairs[sorted_word1] and word2 not in checked_pairs[sorted_word2]:
                anagram_count += 1
                checked_pairs[sorted_word1].add(word1)
                checked_pairs[sorted_word2].add(word2)
        if anagram_count > 401:
            return False
    return True