import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[:6] if c.isalpha() and c.isascii()]
    letters = ''.join(letters).lower()
    if len(letters) < 6:
        return set()
    palindromes = set()
    for r in range(6, len(letters) + 1):
        for perm in itertools.permutations(letters, r):
            p = ''.join(perm)
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes