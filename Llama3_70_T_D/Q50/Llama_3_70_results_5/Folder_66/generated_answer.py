from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(lst):
    lst = [''.join(sorted(s.lower())) for s in lst if len(s) >= 3]
    anagrams = defaultdict(list)
    for s in lst:
        anagrams[s].append(s)
    count = 0
    for v in anagrams.values():
        if len(v) > 1:
            count += len(list(combinations(v, 2)))
    return count >= 92