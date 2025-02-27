def palindromes_between_indices(s):
    s = s[1:3].lower()
    palindromes = set()
    for i in range(3, len(s) + 1):
        for p in itertools.permutations(s, i):
            w = ''.join(p)
            if w == w[::-1]:
                palindromes.add(w)
    return palindromes