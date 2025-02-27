from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 6:
        return set()
    substring = ''.join([c.lower() for c in s[:6] if c.isalpha()])
    if len(substring) < 6:
        return set()
    perms = set((''.join(p) for p in permutations(substring)))
    palindromes = set()
    for perm in perms:
        if perm == perm[::-1]:
            palindromes.add(perm)
    return {p for p in palindromes if len(p) >= 6}