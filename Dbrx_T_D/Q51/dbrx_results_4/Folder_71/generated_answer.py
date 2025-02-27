import re

def if_contains_anagrams(string_list):
    anagrams = {}
    for string in string_list:
        sorted_string = ''.join(sorted(re.findall('\\b\\w{3,}\\b', string.lower())))
        if sorted_string in anagrams:
            anagrams[sorted_string] += 1
            if anagrams[sorted_string] > 9:
                return False
        else:
            anagrams[sorted_string] = 1
    return True