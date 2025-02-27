from collections import defaultdict
from math import comb

def if_contains_anagrams(strings):
    anagrams = defaultdict(int)
    for s in strings:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            anagrams[sorted_s] += 1
    pairs = sum((comb(n, 2) for n in anagrams.values()))
    return pairs <= 57