import re

def return_vowels(str1):
    res = re.findall('[aeiou]', str1[5:])
    return res