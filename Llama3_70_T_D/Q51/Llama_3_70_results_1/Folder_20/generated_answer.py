from collections import defaultdict
from math import comb

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s))
        anagrams[sorted_s].append(s)
    count = 0
    for v in anagrams.values():
        count += comb(len(v), 2)
        if count > 131:
            return False
    return True