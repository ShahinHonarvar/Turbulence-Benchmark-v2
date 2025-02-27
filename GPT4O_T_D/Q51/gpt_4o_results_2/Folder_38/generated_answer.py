from itertools import combinations
from collections import Counter

def if_contains_anagrams(words):
    count = 0
    words = [word.lower() for word in words]
    for word1, word2 in combinations(words, 2):
        if len(word1) >= 3 and len(word2) >= 3:
            if Counter(word1) == Counter(word2):
                count += 1
            if count > 416:
                return False
    return True