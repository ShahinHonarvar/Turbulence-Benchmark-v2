import re

def return_vowels(s):
    res = re.findall('[aeiou]{22,82}', s)
    if not res:
        return []
    return res[1:]