import re

def return_vowels(s):
    res = re.findall('[aeiou]', s[31:-2])
    return res