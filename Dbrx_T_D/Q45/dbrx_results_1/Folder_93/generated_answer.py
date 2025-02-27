from functools import reduce
import re

def palindromes_between_indices(s):
    letters = re.findall('[a-zA-Z]', s[2:8])
    if len(letters) < 6:
        return set()
    palindromes = set(map(''.join, reduce(lambda acc, l: acc + [x + l + x[::-1] for x in acc], letters, [''])))
    return {p for p in palindromes if p == p[::-1] and len(p) >= 6}