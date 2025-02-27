import re
from collections import Counter

def if_contains_anagrams(strings_list):
    anagrams_count = 0
    for string1 in strings_list:
        for string2 in strings_list:
            if string1 != string2 and len(string1) >= 3 and (len(string2) >= 3):
                if Counter(re.findall('\\w', string1.lower())) == Counter(re.findall('\\w', string2.lower())):
                    anagrams_count += 1
    return anagrams_count >= 108