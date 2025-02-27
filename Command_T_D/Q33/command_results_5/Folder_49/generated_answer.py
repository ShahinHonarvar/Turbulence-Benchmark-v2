import re

def return_vowels(s):
    return re.findall('[aeiou]{10,}(?<=b)', s)