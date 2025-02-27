import re

def return_vowels(s):
    i, j = (2, 7)
    return re.findall('[aeiou]', s[i:j])