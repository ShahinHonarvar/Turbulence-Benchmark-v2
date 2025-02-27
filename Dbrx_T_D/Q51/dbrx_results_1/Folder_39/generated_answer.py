import re
from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for string in strings:
        sorted_string = ''.join(sorted(re.findall('\\b\\w{3,}\\b', string.lower())))
        anagrams[sorted_string].append(string)
    return sum((len(agram) <= 257 for agram in anagrams.values()))