from collections import defaultdict
from math import comb

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for string in lst:
        lowered = ''.join(filter(str.isalpha, string)).lower()
        if len(lowered) >= 3:
            anagrams[''.join(sorted(lowered))].append(lowered)
    count = sum((comb(len(group), 2) for group in anagrams.values() if len(group) >= 2))
    return count <= 416