import re
from collections import defaultdict

def if_contains_anagrams(string_list):
    anagram_count = 0
    anagrams = defaultdict(list)
    for string in string_list:
        sorted_string = ''.join(sorted(re.findall('\\b\\w+\\b', string.lower())))
        if len(sorted_string) >= 3:
            anagrams[sorted_string].append(string)
            anagram_count += len(anagrams[sorted_string]) - 1
    return anagram_count <= 116