import re

def return_vowels(text):
    return re.findall('[aeiou]', text[641:-1])