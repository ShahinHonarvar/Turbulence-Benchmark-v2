def palindromes_between_indices(s):
    letters = [c.lower() for c in s[:4] if c.isalpha()]
    palindromes = set()
    for i in range(3, len(letters) + 1):
        for combo in itertools.combinations_with_replacement(letters, i):
            permsm = ''.join(combo)
            if permsm == permsm[::-1]:
                palindromes.add(permsm)
    return palindromes