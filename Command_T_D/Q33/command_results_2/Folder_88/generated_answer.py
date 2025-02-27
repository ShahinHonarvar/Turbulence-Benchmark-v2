import re

def return_vowels(text):
    result = re.findall('[aeiou]', text[70:76])
    return result