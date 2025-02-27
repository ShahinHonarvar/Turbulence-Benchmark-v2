import re
from collections import Counter

def if_contains_anagrams(string_list):
    anagram_count = 0
    for string in string_list:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(re.findall('\\\\w', string.lower())))
            anagram_count += len(Counter(sorted_string).keys())
    return anagram_count >= 28 * 2