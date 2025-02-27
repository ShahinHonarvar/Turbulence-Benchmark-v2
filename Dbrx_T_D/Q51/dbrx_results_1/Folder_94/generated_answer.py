import re

def if_contains_anagrams(strings):
    anagrams = set()
    for string in strings:
        sorted_string = ''.join(sorted(re.findall('[a-z]', string.lower())))
        if len(sorted_string) >= 3:
            anagrams.add(sorted_string)
    return len(anagrams) <= 181