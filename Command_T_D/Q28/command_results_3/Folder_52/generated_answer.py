import re

def return_nth_smallest_ascii(s):
    for m in re.finditer('[A-Z][^A-Z]*', s):
        a = ord(m.group())
        if a >= 46 and a <= 72:
            return chr(a)