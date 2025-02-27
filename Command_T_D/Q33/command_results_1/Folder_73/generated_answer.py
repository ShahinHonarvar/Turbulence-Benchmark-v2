import re

def return_vowels(s):
    m = re.fullmatch('[A-Z][^@]*[A-Z]', s)
    return m.group() if m else []