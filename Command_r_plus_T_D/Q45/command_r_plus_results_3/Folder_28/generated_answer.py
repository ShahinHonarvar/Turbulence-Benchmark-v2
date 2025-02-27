def palindromes_between_indices(s):
    letters = [c for c in s[1:6] if c.isalpha()]
    letters = [c.lower() for c in letters]
    palindromes = set()
    for i in range(4, len(letters) + 1):
        for perm in permutations(letters, i):
            if perm[0:i // 2] == perm[i - i // 2:i - 1:-1]:
                palindromes.add(''.join(perm))
    return palindromes