from collections import defaultdict
from math import comb

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for s in lst:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            anagrams[sorted_s].append(s)
    count_pairs = sum((comb(len(v), 2) for v in anagrams.values() if len(v) > 1))
    return count_pairs <= 52