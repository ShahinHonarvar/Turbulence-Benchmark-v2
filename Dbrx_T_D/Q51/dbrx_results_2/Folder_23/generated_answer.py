import re
from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for string in strings:
        sorted_string = ''.join(sorted(re.findall('\\b\\w{3,}\\b', string.lower())))
        anagrams[sorted_string].append(string)
    return len([pair for pair in anagrams.values() if len(pair) > 1]) <= 49