import re

def return_vowels(s):
    return re.findall('[aeiou]b', s)[10:-1]