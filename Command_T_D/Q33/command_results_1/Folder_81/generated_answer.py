import re

def return_vowels(text):
    m = re.match('(\\W){20,43}(?<=\\W)', text)
    if m:
        return m.group(1)
    else:
        return []