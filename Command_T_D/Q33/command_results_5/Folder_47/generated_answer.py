import re

def return_vowels(s):
    return re.findall('[aeiou]([a-z]{,3})', s[23:38])