def palindromes_between_indices(s):
    s = s[4:7].lower()
    palindromes = set()
    for i in range(4, len(s) + 1):
        for perm in itertools.permutations(s, i):
            p = ''.join(perm)
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes