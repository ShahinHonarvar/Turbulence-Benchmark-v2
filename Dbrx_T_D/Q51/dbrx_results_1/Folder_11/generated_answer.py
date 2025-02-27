import re
from collections import Counter

def if_contains_anagrams(list_of_strings):
    anagrams_count = 0
    for string1 in list_of_strings:
        for string2 in list_of_strings:
            if string1 == string2:
                continue
            if len(string1) < 3 or len(string2) < 3:
                continue
            if Counter(re.findall('\\b\\w{3,}\\b', string1.lower())) == Counter(re.findall('\\b\\w{3,}\\b', string2.lower())):
                anagrams_count += 1
                if anagrams_count > 41:
                    return False
    return True