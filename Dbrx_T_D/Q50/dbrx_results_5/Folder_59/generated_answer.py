import re
from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for string in strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(re.findall('\\\\w', string.lower())))
        anagrams[sorted_string].append(string)
    pairs_count = sum((1 for value in anagrams.values() if len(value) >= 2))
    return pairs_count >= 10