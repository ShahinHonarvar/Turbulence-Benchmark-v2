import re

def return_vowels(text):
    return re.findall('([^aieou])([aieou])([^d]?)', text)[1::3]