from collections import defaultdict
from math import comb

def if_contains_anagrams(strings):
    anagrams = defaultdict(int)
    for s in strings:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) >= 3:
            key = ''.join(sorted(s))
            anagrams[key] += 1
    count = sum((comb(v, 2) for v in anagrams.values() if v > 1))
    return count <= 39