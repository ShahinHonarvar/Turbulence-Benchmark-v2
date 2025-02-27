from collections import defaultdict
from math import comb

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        s = s.lower()
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s))
        anagrams[sorted_s].append(s)
    count = 0
    for anagram_group in anagrams.values():
        if len(anagram_group) > 1:
            count += comb(len(anagram_group), 2)
    return count >= 219