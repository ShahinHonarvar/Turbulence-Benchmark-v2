def palindromes_between_indices(s):
    s = s[2:10].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for length in range(6, len(letters) + 1):
        for p in itertools.permutations(letters, length):
            if p == p[::-1]:
                palindromes.add(''.join(p))
    return palindromes