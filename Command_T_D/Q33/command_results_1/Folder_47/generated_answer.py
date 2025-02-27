import re

def return_vowels(s):
    res = re.findall('[aeiou]', s)[23:-1]
    return res