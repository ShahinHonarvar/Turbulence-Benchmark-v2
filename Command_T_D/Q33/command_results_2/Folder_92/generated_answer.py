import re

def return_vowels(string):
    return [m for m in re.finditer('[aeiou]', string[3:-1]) if m.start() >= 3 and m.end() <= 8]