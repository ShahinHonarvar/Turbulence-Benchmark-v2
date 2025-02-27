import re
from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for string in strings:
        string = re.findall('\\b\\w+\\b', string.lower())
        string = ''.join(string)
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string))
            anagrams[sorted_string].append(string)
    pairs_of_anagrams = sum((len(anagrams) for anagrams in anagrams.values() if len(anagrams) > 1))
    return pairs_of_anagrams <= 116