import re

def return_vowels(s):
    return re.findall('[aeiou]([a-z])', s[483:-12])