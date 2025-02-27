import re
from collections import Counter

def if_contains_anagrams(string_list):
    anagrams = []
    for string in string_list:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            if Counter(sorted_string) not in anagrams:
                anagrams.append(Counter(sorted_string))
    return len(anagrams) >= 115