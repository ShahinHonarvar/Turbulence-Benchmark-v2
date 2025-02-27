import re

def return_vowels(str1):
    res = re.findall('[aeiou]', str1[82:-1])
    return res