from itertools import permutations
from string import ascii_lowercase

def palindromes_between_indices(txt):
    idx = txt.find(' ') - 4
    if not idx == 4:
        txt = txt[idx:idx + 5]
    elif txt == '':
        return set()
    letters = (l for l in txt if l.lower() in ascii_lowercase)
    return {p for p in permutations(letters, r=4) if p == p[::-1]}