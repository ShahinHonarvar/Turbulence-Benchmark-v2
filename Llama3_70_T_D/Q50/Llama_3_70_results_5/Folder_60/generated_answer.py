from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        s = s.lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            anagrams[sorted_s].append(s)
    count = 0
    for v in anagrams.values():
        if len(v) > 1:
            count += len(list(combinations(v, 2)))
    return count >= 60