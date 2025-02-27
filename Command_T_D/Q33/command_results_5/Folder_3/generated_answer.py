import re

def return_vowels(s):
    res = re.findall('[aeiou]', s)[1:-1]
    return res