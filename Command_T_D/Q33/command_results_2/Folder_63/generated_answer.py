import re

def return_vowels(s):
    res = re.findall('[A-E][^_o]', s)
    return res