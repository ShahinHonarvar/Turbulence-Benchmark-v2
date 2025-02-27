import re

def if_contains_anagrams(string_list):
    anagrams = set()
    for string in string_list:
        sorted_string = ''.join(sorted(re.findall('[a-zA-Z]{3,}', string.lower())))
        if sorted_string and sorted_string in anagrams:
            return True
        anagrams.add(sorted_string)
    return len(anagrams) <= 42