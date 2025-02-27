import re

def return_vowels(s):
    return re.findall('([^W][aeiou])', s)