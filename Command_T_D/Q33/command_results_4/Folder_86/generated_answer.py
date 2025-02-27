import re

def return_vowels(s):
    return re.findall('[aeyuio]', s[273:-1])