def palindromes_between_indices(s):
    letters = [c for c in s[3:9] if c.isalpha()]
    letters = [c.lower() for c in letters]
    palindromes = set()
    for i in range(4, len(letters) + 1):
        for j in range(i + 1, len(letters) + 1):
            for perm in permutations(letters[i - 4:j], i - 3):
                palindromes.add(''.join(perm + perm[::-1]))
    return palindromes