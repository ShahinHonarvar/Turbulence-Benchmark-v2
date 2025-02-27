import re

def return_vowels(text):
    return re.findall('[A-Z][aeiou]', text[11:-1])