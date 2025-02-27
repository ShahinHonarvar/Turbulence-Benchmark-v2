def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:10] if c.isalpha()]
    palindromes = set()
    for i in range(5, len(letters) + 1):
        for p in itertools.permutations(letters, i):
            w = ''.join(p)
            if w == w[::-1]:
                palindromes.add(w)
    return palindromes