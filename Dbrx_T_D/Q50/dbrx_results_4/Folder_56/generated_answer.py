import re
from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    count = 0
    for string in strings:
        sorted_string = ''.join(sorted(re.findall('\\\\w', string.lower())))
        if len(sorted_string) >= 3:
            anagrams[sorted_string].append(string)
            count += len(anagrams[sorted_string]) - 1
    return count >= 77