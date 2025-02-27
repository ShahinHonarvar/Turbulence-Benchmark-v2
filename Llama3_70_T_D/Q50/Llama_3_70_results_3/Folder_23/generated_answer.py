from collections import defaultdict
from math import comb

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        anagrams[sorted_string].append(string)
    count = 0
    for group in anagrams.values():
        if len(group) > 2:
            count += comb(len(group), 2)
    return count >= 67