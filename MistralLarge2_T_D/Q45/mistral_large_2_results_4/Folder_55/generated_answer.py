import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[:3] if c.isalpha()]
    lower_letters = [c.lower() for c in letters]
    perms = set((''.join(p) for i in range(3, len(lower_letters) + 1) for p in itertools.permutations(lower_letters, i)))
    palindromes = {p for p in perms if p == p[::-1]}
    return palindromes