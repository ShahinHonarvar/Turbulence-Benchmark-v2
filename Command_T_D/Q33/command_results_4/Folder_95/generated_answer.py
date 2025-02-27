import re

def return_vowels(s):
    res = re.findall('[A-Z][^?P]+', s)
    return res