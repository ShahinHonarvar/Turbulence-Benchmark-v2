def palindromes_between_indices(string):
    letters = ''.join((c for c in string[4:10] if c.isalpha())).lower()
    return {''.join(perm) for i in range(4, len(letters) + 1) for perm in itertools.permutations(letters, i) if ''.join(perm) == ''.join(perm)[::-1]}