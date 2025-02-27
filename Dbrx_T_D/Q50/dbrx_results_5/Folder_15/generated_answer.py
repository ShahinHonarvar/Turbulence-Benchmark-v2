import re
from collections import defaultdict

def if_contains_anagrams(string_list):
    anagrams = defaultdict(list)
    for string in string_list:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(re.findall('\\\\w', string.lower())))
        anagrams[sorted_string].append(string)
    anagram_pairs = [pair for pair in anagrams.values() if len(pair) >= 2]
    return len(anagram_pairs) >= 4