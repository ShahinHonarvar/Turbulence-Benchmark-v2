import re

def palindromes_between_indices(s):
    s = s[1:9].lower()
    chars = set(s)
    palindromes = set()
    for c in chars:
        if s.count(c) >= 7:
            palindromes.add(c * 7)
        elif s.count(c) + s.count(c.upper()) >= 7:
            palindromes.add(c * 4 + c.upper() + c.upper() + c)
    return palindromes