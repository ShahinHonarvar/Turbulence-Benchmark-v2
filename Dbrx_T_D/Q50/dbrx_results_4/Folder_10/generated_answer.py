import re
from collections import Counter

def if_contains_anagrams(string_list):
    anagram_count = 0
    for string1 in string_list:
        for string2 in string_list:
            if string1 != string2 and len(string1) >= 3 and (len(string2) >= 3):
                if Counter(re.findall('\\\\w', string1.lower())) == Counter(re.findall('\\\\w', string2.lower())):
                    anagram_count += 1
    return anagram_count >= 52