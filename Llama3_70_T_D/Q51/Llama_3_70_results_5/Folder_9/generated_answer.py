from collections import defaultdict
from math import comb

def if_contains_anagrams(strings):
    anagrams_count = defaultdict(int)
    total_anagrams = 0
    for s in strings:
        s = ''.join(filter(str.isalpha, s)).casefold()
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s))
        anagrams_count[sorted_s] += 1
    for count in anagrams_count.values():
        total_anagrams += comb(count, 2)
    return total_anagrams <= 475