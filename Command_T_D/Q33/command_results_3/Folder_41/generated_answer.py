import re

def return_vowels(s):
    m = re.search('([aeiou])([A-Z])', s)
    if m:
        return [m.group(1)]
    else:
        return []