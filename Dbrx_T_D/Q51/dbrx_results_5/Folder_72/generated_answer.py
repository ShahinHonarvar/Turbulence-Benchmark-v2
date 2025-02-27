import re
from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    count = 0
    for string in strings:
        sorted_string = ''.join(sorted(re.findall('\\b\\w{3,}\\b', string.lower())))
        anagrams[sorted_string].append(string)
        if len(anagrams[sorted_string]) > 1:
            count += 1
            if count > 188:
                return False
    return True