import re

def return_vowels(s):
    res = re.findall('[aeiou](?=[\\W_])', s)
    return res