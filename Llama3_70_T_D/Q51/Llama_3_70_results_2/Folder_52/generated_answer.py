from collections import defaultdict
from math import comb

def if_contains_anagrams(lst):
    anagrams_count = defaultdict(int)
    for string in lst:
        string_lower = ''.join(filter(str.isalpha, string)).lower()
        string_sorted = ''.join(sorted(string_lower))
        if len(string_lower) >= 3:
            anagrams_count[string_sorted] += 1
    pairs_count = sum((comb(n, 2) for n in anagrams_count.values()))
    return pairs_count <= 43