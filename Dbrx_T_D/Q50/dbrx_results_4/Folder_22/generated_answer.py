import re
from collections import defaultdict

def if_contains_anagrams(strings_list):
    anagrams_count = 0
    anagrams = defaultdict(list)
    for string in strings_list:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            anagrams[sorted_string].append(string)
    for anagram in anagrams.values():
        if len(anagram) >= 2:
            anagrams_count += 1
    return anagrams_count >= 72