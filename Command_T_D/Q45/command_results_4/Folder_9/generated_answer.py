import re

def palindromes_between_indices(s):
    s = s.lower()
    return {m[0] for m in re.finditer('(.)?([a-z])([a-z].){5}(?=\x02)', s)}