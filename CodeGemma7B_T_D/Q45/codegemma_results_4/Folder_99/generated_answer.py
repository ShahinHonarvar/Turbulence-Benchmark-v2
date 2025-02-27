from itertools import permutations
  import re

def palindromes_between_indices(txt):
    eng = 'abcdefghijklmnopqrstuvwxyz'
    s = re.findall(f'[{eng}]+', txt)[0].lower()
    s = s[4:9]
    if not s:
        return set()
    return {(''.join(p), ''.join(p[::-1])) for p in permutations(s) if ''.join(p) != ''.join(p[::-1])}