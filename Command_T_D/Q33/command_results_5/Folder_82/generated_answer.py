import re

def return_vowels(s):
    return re.findall('[AEIOU]{86,99}r', s)