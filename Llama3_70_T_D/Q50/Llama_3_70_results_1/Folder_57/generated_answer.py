from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    pairs = set()
    for s in lst:
        s_lower = s.lower()
        if len(s_lower) < 3:
            continue
        sorted_s = ''.join(sorted(s_lower))
        anagrams[sorted_s].append(s_lower)
    for v in anagrams.values():
        if len(v) > 1:
            for p in combinations(v, 2):
                pairs.add(tuple(sorted(p)))
    return len(pairs) >= 50