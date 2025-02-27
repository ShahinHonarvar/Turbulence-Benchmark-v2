import re

def return_vowels(s):
    return re.findall('[aeiou]', s[328:-1])