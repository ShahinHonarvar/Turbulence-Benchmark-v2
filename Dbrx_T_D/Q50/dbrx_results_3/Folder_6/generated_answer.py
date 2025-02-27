import re
from collections import defaultdict

def if_contains_anagrams(strings_list):
    anagrams_count = defaultdict(int)
    for string in strings_list:
        sorted_string = ''.join(sorted(re.findall('\\\\b\\\\w+\\\\b', string.lower())))
        if len(sorted_string) >= 3:
            anagrams_count[sorted_string] += 1
    return sum((value >= 2 for value in anagrams_count.values())) >= 26