import re
from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for string in strings:
        sorted_string = tuple(sorted(re.findall('[A-Za-z]{3,}', string.lower())))
        anagrams[sorted_string].append(string)
    pairs = 0
    for anagram in anagrams.values():
        pairs += len(anagram) * (len(anagram) - 1) // 2
    return pairs >= 140