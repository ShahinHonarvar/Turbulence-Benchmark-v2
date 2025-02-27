from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_count = 0
    checked_pairs = set()
    for s1, s2 in combinations(strings, 2):
        if len(s1) >= 3 and len(s2) >= 3 and is_anagram(s1, s2):
            pair = tuple(sorted((s1.lower(), s2.lower())))
            if pair not in checked_pairs:
                checked_pairs.add(pair)
                anagram_count += 1
                if anagram_count > 475:
                    return False
    return True