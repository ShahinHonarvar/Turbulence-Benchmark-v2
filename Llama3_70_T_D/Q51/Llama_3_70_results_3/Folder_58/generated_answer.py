from collections import defaultdict
from math import comb

def if_contains_anagrams(list_of_strings):
    anagram_dict = defaultdict(int)
    for string in list_of_strings:
        string = ''.join(filter(str.isalpha, string)).lower()
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string))
        anagram_dict[sorted_string] += 1
    num_anagram_pairs = sum((comb(count, 2) for count in anagram_dict.values()))
    return num_anagram_pairs <= 60