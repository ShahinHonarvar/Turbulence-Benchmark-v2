import re

def return_vowels(s):
    for m in re.finditer('[aeiou](?![aieou])', s):
        yield m.group()