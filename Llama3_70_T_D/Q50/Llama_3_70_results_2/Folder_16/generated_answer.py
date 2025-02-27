from itertools import combinations
from collections import Counter

def if_contains_anagrams(strings):
    anagram_pairs = 0
    for s1, s2 in combinations(strings, 2):
        if len(s1) >= 3 and len(s2) >= 3 and (Counter(s1.lower()) == Counter(s2.lower())):
            anagram_pairs += 1
    return anagram_pairs >= 155