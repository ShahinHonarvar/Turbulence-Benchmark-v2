def palindromes_between_indices(s):
    s = s[1:9]
    palindromes = set()
    for i in range(4, len(s) + 1):
        for p in permutations(s, i):
            if p == p[::-1]:
                palindromes.add(p.lower())
    return palindromes if palindromes else set()