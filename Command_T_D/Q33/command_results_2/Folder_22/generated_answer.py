import re

def return_vowels(s):
    return re.findall('[A-Z][^KZ]', s)