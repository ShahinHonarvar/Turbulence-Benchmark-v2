import re

def return_vowels(text):
    return [c for c in text if c.isalpha() and c.isupper() and (c in re.findall('[A-Z][^<z]'))]