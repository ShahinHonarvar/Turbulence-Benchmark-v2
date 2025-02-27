import re

def return_vowels(s):
    return re.findall('(([aeiou])\\w+)', s)[1:-1]