from itertools import combinations
from collections import Counter

def if_contains_anagrams(words):
    words = [word.lower() for word in words]

    def is_anagram(word1, word2):
        return Counter(word1) == Counter(word2)
    words = [word for word in words if len(word) >= 3 and word.isalpha()]
    anagram_pairs = 0
    for word1, word2 in combinations(words, 2):
        if is_anagram(word1, word2):
            anagram_pairs += 1
            if anagram_pairs > 464:
                return False
    return True