from collections import defaultdict
from math import comb

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            anagrams[sorted_s].append(s)
    pairs = 0
    for v in anagrams.values():
        pairs += comb(len(v), 2)
        if pairs > 77:
            return False
    return True