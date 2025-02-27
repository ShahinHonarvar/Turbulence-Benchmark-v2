import itertools
from collections import Counter

def if_contains_anagrams(lst):
    cnt = Counter()
    for s in lst:
        if len(s) >= 3:
            cnt[tuple(sorted(s.lower()))] += 1
    pairs = sum((v * (v - 1) // 2 for v in cnt.values() if v >= 2))
    return pairs <= 21