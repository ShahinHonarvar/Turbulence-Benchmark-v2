import re

def return_vowels(s):
    return re.findall('[A-U]+', s, flags=re.I)