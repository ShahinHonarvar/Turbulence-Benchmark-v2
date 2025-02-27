import re

def return_vowels(s):
    res = re.findall('[aeiou](?=[dD])[a-v]', s)
    return res