from itertools import permutations
    from string import ascii_lowercase

def palindromes_between_indices(s):
    s = ''.join((c for i, c in enumerate(s) if 1 <= i <= 8 and c.lower() in ascii_lowercase))
    pals = set((''.join(p) for r in range(7, len(s) + 1) for p in permutations(s, r) if ''.join(p) == ''.join(p)[::-1]))
    return pals