import re

def return_vowels(s):
    return re.findall('([aeiou])\\B', s[40:-1])