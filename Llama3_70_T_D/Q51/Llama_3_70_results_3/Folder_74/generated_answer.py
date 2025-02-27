from collections import defaultdict
from math import comb

def if_contains_anagrams(strings):
    anagrams_count = defaultdict(int)
    for s in strings:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s))
        anagrams_count[sorted_s] += 1
    pairs_count = sum((comb(val, 2) for val in anagrams_count.values() if val > 1))
    return pairs_count <= 57