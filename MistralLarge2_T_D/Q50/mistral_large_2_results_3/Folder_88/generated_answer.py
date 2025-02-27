from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(strings):
    anagram_map = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            key = ''.join(sorted(s.lower()))
            anagram_map[key].append(s)
    anagram_pairs = sum((len(group) * (len(group) - 1) // 2 for group in anagram_map.values() if len(group) > 1))
    return anagram_pairs >= 34