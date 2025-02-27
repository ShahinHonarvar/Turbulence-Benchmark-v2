def palindromes_between_indices(s):
    if not isinstance(s, str):
        return 'Input must be a string.'
    substring = s[6:10].lower() if len(s) >= 10 else ''
    if not all((c.isalpha() for c in substring)):
        return 'There are no English letters between the specified indices.'
    perms = [''.join(p) for i in range(len(substring), 0, -1) for p in itertools.permutations(substring, i)]
    palindromes = [perm for perm in perms if len(perm) >= 5 and perm == perm[::-1]]
    return set(palindromes)