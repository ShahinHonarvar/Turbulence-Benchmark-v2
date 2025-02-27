import re

def return_vowels(s):
    res = re.findall('[aeiou]', s[20:34])
    return res