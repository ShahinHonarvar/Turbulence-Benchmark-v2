import re
from collections import defaultdict

def if_contains_anagrams(strings_list):
    anagrams_count = 0
    anagrams_dict = defaultdict(set)
    for string in strings_list:
        sorted_string = ''.join(sorted(re.findall('[a-z]{3,}', string.lower())))
        anagrams_dict[sorted_string].add(string)
    for anagrams in anagrams_dict.values():
        anagrams_count += len(anagrams) * (len(anagrams) - 1) // 2
    return anagrams_count <= 392