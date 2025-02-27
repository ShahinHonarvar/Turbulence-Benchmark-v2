import re

def return_vowels(s):
    m = re.fullmatch('<[a-z]*>', s)
    if m:
        return m.group()
    else:
        return ['']