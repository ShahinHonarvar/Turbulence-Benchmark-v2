from collections import defaultdict
from math import comb

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        s_lower = ''.join(filter(str.isalpha, s.lower()))
        if len(s_lower) < 3:
            continue
        sorted_s = ''.join(sorted(s_lower))
        anagrams[sorted_s].append(s)
    pairs = sum((comb(len(anagrams[k]), 2) for k in anagrams if len(anagrams[k]) > 1))
    return pairs <= 47