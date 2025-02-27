from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_pairs = 0
    checked_pairs = set()
    for s1, s2 in combinations(strings, 2):
        if (s1, s2) in checked_pairs or (s2, s1) in checked_pairs:
            continue
        checked_pairs.add((s1, s2))
        if len(s1) >= 3 and len(s2) >= 3 and is_anagram(s1, s2):
            anagram_pairs += 1
            if anagram_pairs > 464:
                return False
    return True