from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        s_lower = s.lower()
        anagrams[''.join(sorted(s_lower))].append(s_lower)
    pairs = 0
    for v in anagrams.values():
        if len(v) > 1 and len(v[0]) >= 3:
            pairs += len(list(combinations(v, 2)))
    return pairs >= 79