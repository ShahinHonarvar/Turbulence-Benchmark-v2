import re
from collections import defaultdict

def if_contains_anagrams(list_of_strings):
    anagrams = defaultdict(list)
    for string in list_of_strings:
        sorted_string = ''.join(sorted(re.findall('\\b\\w{3,}\\b', string.lower())))
        anagrams[sorted_string].append(string)
    return sum((len(value) > 25 for value in anagrams.values())) > 0