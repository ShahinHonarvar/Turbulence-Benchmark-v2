from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(strings):
    anagram_map = defaultdict(list)
    for s in strings:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            anagram_map[sorted_s].append(s)
    anagram_pairs = 0
    for anagrams in anagram_map.values():
        anagram_pairs += len(list(combinations(anagrams, 2)))
    return anagram_pairs <= 59