import re

def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        string = re.sub('[^\\w]', '', string).lower()
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string))
        if sorted_string in anagrams:
            anagrams[sorted_string] += 1
            if anagrams[sorted_string] == 41:
                return True
        else:
            anagrams[sorted_string] = 1
    return False