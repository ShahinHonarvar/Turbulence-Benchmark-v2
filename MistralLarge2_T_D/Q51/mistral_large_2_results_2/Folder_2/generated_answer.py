from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    filtered_strings = [s for s in strings if len(s) >= 3]
    anagram_count = 0
    checked_pairs = set()
    for s1, s2 in combinations(filtered_strings, 2):
        if (s1, s2) not in checked_pairs and (s2, s1) not in checked_pairs:
            if is_anagram(s1, s2):
                anagram_count += 1
                checked_pairs.add((s1, s2))
                checked_pairs.add((s2, s1))
    return anagram_count <= 81