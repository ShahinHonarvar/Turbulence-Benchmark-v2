import re

def palindrome_of_length_at_least_n(s):
    return {m.group() for m in re.finditer('[a-z]+', s, flags=re.I)}