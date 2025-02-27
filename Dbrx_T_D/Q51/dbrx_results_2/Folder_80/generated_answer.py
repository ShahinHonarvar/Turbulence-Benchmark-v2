import re

def if_contains_anagrams(string_list):
    anagrams = set()
    for string in string_list:
        if len(string) < 3 or not string.isalpha():
            continue
        sorted_string = ''.join(sorted(re.findall('[a-z]', string.lower())))
        if len(sorted_string) < 3:
            continue
        anagrams.add(sorted_string)
    return len(anagrams) <= 255