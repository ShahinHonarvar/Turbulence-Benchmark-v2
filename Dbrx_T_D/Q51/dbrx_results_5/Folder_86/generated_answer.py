import re
from collections import defaultdict

def if_contains_anagrams(string_list):
    anagrams = defaultdict(list)
    for string in string_list:
        sorted_string = ''.join(sorted(re.findall('[a-z]', string.lower())))
        anagrams[sorted_string].append(string)
    anagram_pairs = sum((1 for value in anagrams.values() if len(value) >= 3))
    return anagram_pairs <= 48