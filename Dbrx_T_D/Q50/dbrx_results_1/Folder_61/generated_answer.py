import re
from collections import defaultdict

def if_contains_anagrams(strings_list):
    anagrams_dict = defaultdict(list)
    for string_ele in strings_list:
        if len(string_ele) >= 3:
            sorted_string = ''.join(sorted(string_ele.lower()))
            anagrams_dict[sorted_string].append(string_ele)
    count = sum((1 for value in anagrams_dict.values() if len(value) >= 2))
    return count >= 8