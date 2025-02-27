from itertools import combinations
from collections import Counter

def if_contains_anagrams(str_list):
    str_list = [s.lower() for s in str_list]
    sorted_str_list = sorted(str_list, key=len)
    str_count = Counter(sorted_str_list)
    anagram_count = 0
    for char_count in str_count.values():
        if char_count >= 49:
            anagram_count += combination(char_count, 3)
    return anagram_count >= 49