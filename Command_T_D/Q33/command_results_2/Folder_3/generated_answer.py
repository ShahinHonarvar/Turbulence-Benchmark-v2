import re

def return_vowels(string):
    m = re.findall('[aeiou]', string[50:-1])
    return m