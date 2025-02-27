import re

def return_vowels(s):
    return re.findall('[AEIO]', s[1:-1])