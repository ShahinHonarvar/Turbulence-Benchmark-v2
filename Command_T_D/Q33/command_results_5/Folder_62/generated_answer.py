import re

def return_vowels(s):
    return re.findall('[aeiou]([A-Z]?)', s)[1:]