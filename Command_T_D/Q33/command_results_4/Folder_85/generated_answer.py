import re

def return_vowels(s):
    v = re.findall('[aeiou]', s[55:-1])
    return v