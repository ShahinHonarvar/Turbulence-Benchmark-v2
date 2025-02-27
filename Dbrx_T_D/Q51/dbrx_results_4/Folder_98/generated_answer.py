import re
from collections import Counter

def if_contains_anagrams(strings):
    anagrams = []
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(re.findall('[a-zA-Z]', string.lower())))
            if sorted_string not in anagrams:
                anagrams.append(sorted_string)
    return len(anagrams) <= 46