import re

def return_vowels(s):
    return [m.group() for m in re.finditer('<(e|i|o|u)', s, flags=re.I)]