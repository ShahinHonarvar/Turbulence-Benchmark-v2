import re

def palindromes_between_indices(s):
    return {m.group() for m in re.finditer('[a-z]{4}(?=\\w){4}[a-z]{4}', s[4:-5])}