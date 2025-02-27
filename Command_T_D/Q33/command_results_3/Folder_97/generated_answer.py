import re

def return_vowels(str1):
    res = re.findall('[aeiou]', str1[328:455])
    return res