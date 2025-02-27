import re
from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for string in strings:
        sorted_string = ''.join(sorted(re.findall('[a-zA-Z]{3,}', string.lower())))
        anagrams[sorted_string].append(string)
    return sum((1 for value in anagrams.values() if len(value) > 4)) == 0