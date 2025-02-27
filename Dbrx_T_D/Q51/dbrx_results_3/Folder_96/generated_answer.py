import re

def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        string = re.sub('\\W+', '', string).lower()
        sorted_string = ''.join(sorted(string))
        if len(string) < 3:
            continue
        if sorted_string in anagrams:
            anagrams[sorted_string] += 1
            if anagrams[sorted_string] > 2:
                return False
        else:
            anagrams[sorted_string] = 1
    return True