def palindromes_between_indices(string):
    letters = ''.join((c for c in string[2:8] if c.isalpha())).lower()
    return {''.join(perm) for i in range(3, len(letters) + 1) for perm in itertools.permutations(letters, i) if ''.join(perm) == ''.join(perm)[::-1]}