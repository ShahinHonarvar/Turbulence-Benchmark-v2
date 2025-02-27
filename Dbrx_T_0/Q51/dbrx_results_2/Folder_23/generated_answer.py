import re
from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for string in strings:
        sorted_string = ''.join(sorted(re.findall('\\\\b\\\\w+\\\\b', string.lower())))
        if len(sorted_string) >= 3:
            anagrams[sorted_string].append(string)
    return sum((len(value) > 1 for value in anagrams.values())) <= 49