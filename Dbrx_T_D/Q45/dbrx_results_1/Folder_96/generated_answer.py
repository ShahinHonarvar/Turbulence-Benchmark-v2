def palindromes_between_indices(s):
    letters = set(s[3:9].lower())
    palindromes = set()
    for length in range(6, len(letters) + 1):
        permutations = itertools.permutations(letters, length)
        for perm in permutations:
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes