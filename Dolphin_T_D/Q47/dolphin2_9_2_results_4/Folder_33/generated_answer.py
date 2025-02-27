import re

def palindromes_of_specific_lengths(s):
    substring = s[130:295]
    palindromes = set(re.findall('[A-Za-z]{103,158}', substring))
    return set(filter(lambda p: p == p.lower() and p[::-1] == p, palindromes))