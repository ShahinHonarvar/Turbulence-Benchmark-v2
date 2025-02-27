import re

def return_vowels(s):
    res = re.findall('[aeiou]', s)[10:-1]
    if not res:
        return []
    return res