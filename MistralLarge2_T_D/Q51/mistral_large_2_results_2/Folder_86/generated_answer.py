from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_count = 0
    length_filtered = [s for s in strings if len(s) >= 3]
    for s1, s2 in combinations(length_filtered, 2):
        if is_anagram(s1, s2):
            anagram_count += 1
    return anagram_count <= 48