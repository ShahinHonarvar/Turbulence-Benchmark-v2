import re

def return_vowels(s):
    m = re.match('(?<=.)[aeiou]', s[10:83])
    if m:
        return m.group()
    else:
        return []