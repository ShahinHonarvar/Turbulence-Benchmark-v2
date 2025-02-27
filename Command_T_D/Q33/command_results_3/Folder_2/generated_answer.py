import re

def return_vowels(str):
    return re.findall('[aeiou]', str[170:-1])