from collections import defaultdict
from itertools import combinations

def count_anagrams(str_list):
    str_dict = defaultdict(list)
    for string in str_list:
        sorted_str = ''.join(sorted(string.lower()))
        str_dict[sorted_str].append(string)
    pair_count = 0
    for anagram_list in str_dict.values():
        for pair in combinations(anagram_list, 2):
            pair_count += 1
    return pair_count <= 113

def if_contains_anagrams(str_list):
    return count_anagrams(str_list)