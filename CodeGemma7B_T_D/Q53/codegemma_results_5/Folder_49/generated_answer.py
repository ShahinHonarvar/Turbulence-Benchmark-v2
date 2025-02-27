import re

def palindrome_of_length_at_least_n(s):
    p = '[A-Za-z]{73,}'
    return set((m.group(0) for m in re.finditer(p, s, re.IGNORECASE)))