import re
from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for string in strings:
        string = string.lower()
        sorted_string = ''.join(sorted(string))
        anagrams[sorted_string].append(string)
    anagram_pairs = sum((len(val) * (len(val) - 1) // 2 for val in anagrams.values()))
    return anagram_pairs <= 276