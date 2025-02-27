import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[1:9] if c.isalpha()]
    if len(letters) < 4:
        return set()
    perms = set((''.join(p) for i in range(4, len(letters) + 1) for p in itertools.permutations(letters, i)))
    palindromes = {''.join(p).lower() for p in perms if p == p[::-1]}
    return palindromes