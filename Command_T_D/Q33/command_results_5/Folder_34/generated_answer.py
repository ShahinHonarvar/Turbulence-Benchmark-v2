import re

def return_vowels(s):
    return re.findall('[aeiou]([19-32])[0-7]', s)