import re

def return_vowels(str):
    m = re.match('[aeyuio]+', str)
    return m.group() if m else []