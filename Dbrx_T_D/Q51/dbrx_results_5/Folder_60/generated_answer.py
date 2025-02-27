import re

def if_contains_anagrams(list_of_strings):
    anagrams = {}
    count = 0
    for string in list_of_strings:
        string = string.lower()
        sorted_string = ''.join(sorted(re.findall('\\b\\w{3,}\\b', string)))
        if sorted_string in anagrams:
            anagrams[sorted_string] += 1
            if anagrams[sorted_string] == 2:
                count += 1
                if count > 77:
                    return False
        else:
            anagrams[sorted_string] = 1
    return True