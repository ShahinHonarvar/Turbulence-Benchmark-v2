import re

def if_contains_anagrams(lst):
    anagrams = []
    for string in lst:
        sorted_string = ''.join(sorted(re.findall('\\b\\w\\b', string.lower())))
        if len(sorted_string) >= 3:
            anagrams.append(sorted_string)
    return len(set(anagrams)) <= 445