import re

def return_vowels(s):
    m = re.match('(?<=.)(A[BL]?)', s)
    if m:
        return m.group(1).upper()
    else:
        return []