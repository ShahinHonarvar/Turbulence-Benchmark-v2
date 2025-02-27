from collections import defaultdict
from itertools import combinations

def if_contains_anagrams(str_list):
    str_dict = defaultdict(int)
    for string in str_list:
        str_dict[tuple(sorted([char for char in string.lower() if char.isalpha() and len(char) >= 3]))] += 1
    count = 0
    for k, v in str_dict.items():
        count += v * (v - 1) // 2
    return count <= 42