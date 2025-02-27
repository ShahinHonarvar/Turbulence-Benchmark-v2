import re

def return_vowels(s):
    return re.findall('[A-EIOU]', s[528:606])