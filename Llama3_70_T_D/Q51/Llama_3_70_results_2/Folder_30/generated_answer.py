from collections import defaultdict
from math import comb

def if_contains_anagrams(strings):
    anagrams_count = defaultdict(int)
    n = len(strings)
    for string in strings:
        original_string = string
        string = ''.join(filter(str.isalpha, string)).lower()
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string))
        if original_string != string:
            anagrams_count[sorted_string] += 1
    pairs_of_anagrams = sum((comb(count, 2) for count in anagrams_count.values()))
    return pairs_of_anagrams <= 28