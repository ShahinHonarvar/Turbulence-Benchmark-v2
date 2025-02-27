import re
from collections import Counter

def if_contains_anagrams(string_list):
    anagram_count = 0
    for string in string_list:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(re.findall('\\b\\w{3,}\\b', string.lower())))
            if sorted_string in anagram_dict:
                anagram_dict[sorted_string] += 1
                if anagram_dict[sorted_string] == 2:
                    anagram_count += 1
            else:
                anagram_dict[sorted_string] = 1
    return anagram_count <= 14