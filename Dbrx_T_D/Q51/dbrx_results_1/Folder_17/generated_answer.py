import re
from collections import defaultdict

def if_contains_anagrams(list_of_strings):
    anagrams = defaultdict(list)
    for string in list_of_strings:
        sorted_string = ''.join(sorted(re.findall('\\b\\w+\\b', string.lower())))
        if len(sorted_string) >= 3:
            anagrams[sorted_string].append(string)
    pairs = 0
    for anagram in anagrams.values():
        pairs += len(anagram) * (len(anagram) - 1) // 2
    return pairs <= 22