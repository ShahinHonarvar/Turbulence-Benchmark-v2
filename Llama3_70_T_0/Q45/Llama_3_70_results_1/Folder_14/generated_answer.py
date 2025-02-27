def palindromes_between_indices(s):
    s = s[4:6].lower()
    palindromes = set()
    for i in range(3, len(s) + 1):
        for p in [''.join(p) for p in itertools.permutations(s, i) if p == p[::-1]]:
            palindromes.add(p)
    return palindromes