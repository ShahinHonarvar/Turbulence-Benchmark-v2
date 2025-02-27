import re

def return_vowels(s):
    return [m.group() for m in re.finditer('[aeiou]{2,3}', s[40:91])]