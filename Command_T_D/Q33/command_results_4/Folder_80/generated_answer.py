import re

def return_vowels(s):
    m = re.search('((?<=\\W)[aeiou])(\\W)', s)
    return m.group(1) if m else []