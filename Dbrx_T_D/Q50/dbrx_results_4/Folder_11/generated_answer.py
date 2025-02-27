import re
from collections import defaultdict

def if_contains_anagrams(strings_list):
    anagrams_count = 0
    anagrams_dict = defaultdict(list)
    for string in strings_list:
        sorted_string = ''.join(sorted(re.findall('\\\\w', string.lower())))
        anagrams_dict[sorted_string].append(string)
    for anagrams_list in anagrams_dict.values():
        if len(anagrams_list) >= 3:
            anagrams_count += len(anagrams_list) - 1
    return anagrams_count >= 28