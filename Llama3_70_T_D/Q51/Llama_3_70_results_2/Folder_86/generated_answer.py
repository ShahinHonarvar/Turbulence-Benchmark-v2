from collections import defaultdict
from math import comb

def if_contains_anagrams(strings):
    anagram_count = defaultdict(int)
    total_anagram_pairs = 0
    for s in strings:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            anagram_count[sorted_s] += 1
    for count in anagram_count.values():
        if count > 1:
            total_anagram_pairs += comb(count, 2)
    return total_anagram_pairs <= 48