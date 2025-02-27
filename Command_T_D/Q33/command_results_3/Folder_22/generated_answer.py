import re

def return_vowels(text):
    return [m.group() for m in re.finditer('[aeiou]', text[56:90]) if m.group() > 'k' and m.group() <= 'z']