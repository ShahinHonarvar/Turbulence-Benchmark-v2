import re

def return_vowels(s):
    m = re.match('<\\d\\d>([aeiou])', s)
    return [m.group(1)] if m else []