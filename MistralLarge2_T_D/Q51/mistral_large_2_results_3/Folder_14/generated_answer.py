from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s.lower()))
        anagrams[sorted_s].append(s)
    pairs = 0
    for group in anagrams.values():
        if len(group) > 1:
            pairs += len(list(combinations(group, 2)))
    return pairs <= 474