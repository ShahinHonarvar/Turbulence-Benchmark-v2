from collections import defaultdict
from math import comb

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) < 3:
            continue
        sorted_str = ''.join(sorted(s))
        anagrams[sorted_str].append(s)
    count = sum((comb(len(lst), 2) for lst in anagrams.values() if len(lst) > 1))
    return count <= 147