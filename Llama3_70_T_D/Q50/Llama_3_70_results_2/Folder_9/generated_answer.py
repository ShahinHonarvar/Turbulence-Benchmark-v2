from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        s_lower = s.lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s_lower))
            anagrams[sorted_s].append(s_lower)
    count = 0
    for v in anagrams.values():
        if len(v) > 1:
            count += len(list(combinations(v, 2)))
    return count >= 66