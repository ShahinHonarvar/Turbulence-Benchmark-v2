import re

def return_vowels(s):
    m = re.match('(?<=.)([aeiou])', s[770:852])
    return [m.group(1)]