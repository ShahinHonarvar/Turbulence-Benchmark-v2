import re

def return_vowels(s):
    res = re.findall('[A-E][^b]*[A-O]', s)
    return res