import re

def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        string = re.sub('\\W+', '', string).lower()
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string))
        if sorted_string in anagrams:
            anagrams[sorted_string].append(string)
        else:
            anagrams[sorted_string] = [string]
    for value in anagrams.values():
        if len(value) >= 2:
            return True
    return False