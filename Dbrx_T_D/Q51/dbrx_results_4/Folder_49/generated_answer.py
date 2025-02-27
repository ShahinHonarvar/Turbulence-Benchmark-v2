import re

def if_contains_anagrams(string_list):
    anagrams = {}
    count = 0
    for string in string_list:
        sorted_string = ''.join(sorted(re.findall('\\b\\w+\\b', string.lower())))
        if len(sorted_string) >= 3:
            if sorted_string in anagrams:
                anagrams[sorted_string] += 1
                count += 1
                if count > 10:
                    return False
            else:
                anagrams[sorted_string] = 1
    return True