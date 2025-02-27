from collections import defaultdict
from math import comb

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        s_lower = s.lower()
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s_lower))
            anagrams[sorted_str].append(s_lower)
    count = sum((comb(len(v), 2) for v in anagrams.values() if len(v) > 1))
    return count >= 54