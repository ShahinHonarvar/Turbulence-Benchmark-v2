from collections import Counter
from itertools import combinations

def if_contains_anagrams(lst):
    anagram_pairs = 0
    for i, j in combinations(lst, 2):
        if len(i) < 3 or len(j) < 3:
            continue
        if Counter(i.lower()) == Counter(j.lower()):
            anagram_pairs += 1
    return anagram_pairs >= 58