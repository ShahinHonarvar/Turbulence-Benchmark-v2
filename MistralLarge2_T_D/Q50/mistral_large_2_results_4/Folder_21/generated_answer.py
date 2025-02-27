from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(string_list):
    anagram_dict = defaultdict(list)
    for string in string_list:
        sorted_str = ''.join(sorted(string.lower()))
        if len(sorted_str) >= 3:
            anagram_dict[sorted_str].append(string)
    anagram_pairs_count = 0
    for key in anagram_dict:
        if len(anagram_dict[key]) > 1:
            anagram_pairs_count += len(list(combinations(anagram_dict[key], 2)))
    return anagram_pairs_count >= 136