import re

def return_vowels(s):
    m = re.search('<74,96>([aeiou])<I,X>', s)
    if m:
        return m.group(1)
    else:
        return []