from collections import defaultdict
from math import comb

def if_contains_anagrams(list_of_strings):
    anagram_dict = defaultdict(int)
    for string in list_of_strings:
        lower_string = string.lower()
        sorted_string = ''.join(sorted(filter(str.isalpha, lower_string)))
        if len(sorted_string) >= 3:
            anagram_dict[sorted_string] += 1
    pairs = sum((comb(count, 2) for count in anagram_dict.values()))
    return pairs <= 48