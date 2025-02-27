import re

def return_vowels(text):
    return re.findall('[aeiou]', text[5:-1])