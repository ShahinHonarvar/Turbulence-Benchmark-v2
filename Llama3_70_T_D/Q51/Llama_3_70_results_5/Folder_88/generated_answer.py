from collections import defaultdict
from math import comb

def if_contains_anagrams(lst):
    anagrams = defaultdict(int)
    for s in lst:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            anagrams[sorted_s] += 1
    total_anagrams = sum((comb(c, 2) for c in anagrams.values()))
    return total_anagrams <= 407