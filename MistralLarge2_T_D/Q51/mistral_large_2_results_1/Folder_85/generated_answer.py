from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_pairs = 0
    checked_pairs = set()
    for s1, s2 in combinations(strings, 2):
        if len(s1) >= 3 and len(s2) >= 3 and is_anagram(s1, s2):
            sorted_pair = tuple(sorted((s1, s2)))
            if sorted_pair not in checked_pairs:
                anagram_pairs += 1
                checked_pairs.add(sorted_pair)
    return anagram_pairs <= 276