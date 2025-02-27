import re
from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for string in strings:
        sorted_string = ''.join(sorted(re.findall('\\\\b\\\\w+\\\\b', string.lower())))
        anagrams[sorted_string].append(string)
    anagram_pairs = sum((1 for group in anagrams.values() if len(group) >= 3))
    return anagram_pairs <= 210