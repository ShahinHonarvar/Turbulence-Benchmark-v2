import re

def return_vowels(s):
    return re.findall('[A-Z][^B-t]', s[495:837])