import re

def return_vowels(s):
    return re.findall('[AEIOU]', s[74:-3])