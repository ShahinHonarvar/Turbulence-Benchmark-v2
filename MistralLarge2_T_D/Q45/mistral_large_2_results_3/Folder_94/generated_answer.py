def palindromes_between_indices(s):
    chars = set((c.lower() for c in s[3:5] if c.isalpha()))
    palindromes = set()
    for length in range(3, len(chars) + 1):
        for perm in permutations(chars, length):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes