import re
from collections import defaultdict

def if_contains_anagrams(strings_list):
    anagrams_count = 0
    anagrams_dict = defaultdict(list)
    for string in strings_list:
        sorted_string = ''.join(sorted(re.findall('[a-z]', string.lower())))
        anagrams_dict[sorted_string].append(string)
    for value in anagrams_dict.values():
        if len(value) >= 3:
            anagrams_count += len(value) * (len(value) - 1) // 2
    return anagrams_count <= 34