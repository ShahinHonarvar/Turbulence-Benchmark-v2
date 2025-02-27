from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(strings):
    anagram_count = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s.lower()))
            anagram_count[sorted_str].append(s)
    pairs = 0
    for group in anagram_count.values():
        if len(group) > 1:
            pairs += len(list(combinations(group, 2)))
    return pairs >= 93