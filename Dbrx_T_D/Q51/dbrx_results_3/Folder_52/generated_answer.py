import re
from collections import Counter

def if_contains_anagrams(lst):
    anagrams = []
    for string in lst:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(re.findall('\\b\\w+\\b', string.lower())))
            if len(sorted_string) > 1:
                anagrams.append(Counter(sorted_string))
    return len(anagrams) <= 43