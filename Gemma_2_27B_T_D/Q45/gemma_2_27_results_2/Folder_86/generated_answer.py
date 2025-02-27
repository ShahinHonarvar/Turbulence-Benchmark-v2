from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join([c for c in s[6:10] if c.isalpha()])
    return set([''.join(p) for p in permutations(letters) if ''.join(p).lower() == ''.join(p)[::-1].lower() and len(''.join(p)) >= 4])