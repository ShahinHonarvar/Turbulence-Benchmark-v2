import re

def return_vowels(text):
    text = re.sub('[^A-Z0-9]', '', text)
    return [c for c in text[10:-2] if c.isupper() and c.isalpha() and (c in 'AEIOU')]