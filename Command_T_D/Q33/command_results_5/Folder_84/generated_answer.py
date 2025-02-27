import re

def return_vowels(text):
    return re.findall('[aeiou]{3}'.encode(), text[770:-1])