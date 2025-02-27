from itertools import permutations
from collections import Counter

def if_contains_anagrams(str_list):
    str_dict = {}
    for s in str_list:
        s = ''.join(sorted(s.lower()))
        str_dict.setdefault(s, []).append(s)
    anagrams = []
    for v in str_dict.values():
        if len(v) >= 3:
            anagrams.extend(list(permutations(v)))
    return len(anagrams) >= 9