import re
from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for string in strings:
        sorted_string = ''.join(sorted(re.findall('[a-zA-Z]{3,}', string.lower())))
        anagrams[sorted_string].append(string)
    return len(anagrams.values()) <= 89