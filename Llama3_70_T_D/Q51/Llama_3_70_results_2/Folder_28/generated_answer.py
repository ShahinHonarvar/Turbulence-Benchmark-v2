from collections import defaultdict
from math import comb

def if_contains_anagrams(strings):
    anagram_count = defaultdict(int)
    for string in strings:
        lower_string = ''.join(filter(str.isalpha, string)).lower()
        if len(lower_string) >= 3:
            sorted_string = ''.join(sorted(lower_string))
            anagram_count[sorted_string] += 1
    pairs = sum((comb(count, 2) for count in anagram_count.values()))
    return pairs <= 78