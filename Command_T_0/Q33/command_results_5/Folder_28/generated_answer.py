import re

def return_vowels(s):
    return re.findall('[A-Z][^W_]+[A-Z]', s)