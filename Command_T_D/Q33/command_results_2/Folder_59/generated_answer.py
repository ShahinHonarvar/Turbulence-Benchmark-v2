import re

def return_vowels(s):
    return re.findall('[aeiou](?:s|$)', s[8:-1])