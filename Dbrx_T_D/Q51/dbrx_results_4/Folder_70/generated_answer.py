import re

def if_contains_anagrams(list_of_strings):
    anagrams = {}
    for string in list_of_strings:
        sorted_string = ''.join(sorted(re.findall('\\b\\w+\\b', string.lower())))
        if len(sorted_string) >= 3:
            if sorted_string in anagrams:
                anagrams[sorted_string] += 1
                if anagrams[sorted_string] > 97:
                    return False
            else:
                anagrams[sorted_string] = 1
    return True