import re

def return_vowels(s):
    return [x for x in range(23, 38) if re.search('^[aeiou]', s[x:])]