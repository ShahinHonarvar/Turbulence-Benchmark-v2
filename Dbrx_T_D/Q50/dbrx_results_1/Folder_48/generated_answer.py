import re
from collections import Counter

def if_contains_anagrams(strings_list):
    anagrams_count = 0
    for string1 in strings_list:
        if len(string1) < 3:
            continue
        for string2 in strings_list[strings_list.index(string1) + 1:]:
            if len(string2) < 3:
                continue
            if Counter(re.findall('\\\\d+|\\\\D+', string1.lower())) == Counter(re.findall('\\\\d+|\\\\D+', string2.lower())) and string1.lower() != string2.lower():
                anagrams_count += 1
                if anagrams_count >= 219:
                    return True
    return False