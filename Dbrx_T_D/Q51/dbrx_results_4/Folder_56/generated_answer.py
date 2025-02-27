import re

def if_contains_anagrams(string_list):
    anagrams = []
    for string in string_list:
        sorted_string = ''.join(sorted(re.findall('\\b\\w{3,}\\b', string.lower())))
        if sorted_string not in anagrams:
            anagrams.append(sorted_string)
    return len(anagrams) <= 11