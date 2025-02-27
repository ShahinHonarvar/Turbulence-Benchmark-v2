from itertools import permutations

def palindromes_between_indices(s):
    sub = ''.join([c.lower() for c in s[3:6] if c.isalpha()])
    if len(sub) < 3:
        return set()
    perms = set((''.join(p) for p in permutations(sub)))
    palindromes = {p for p in perms if p == p[::-1] and len(p) >= 3}
    return palindromes