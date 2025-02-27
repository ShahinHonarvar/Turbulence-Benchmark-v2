def palindromes_between_indices(s):
    s = [c.lower() for c in s]
    palindromes = set()
    for i in range(3, 9):
        sub = [''] * 6
        for j in range(6):
            sub[j] = s[i + j]
        for p in permutations(sub):
            p = ''.join(p)
            if len(p) >= 4 and p == p[::-1]:
                palindromes.add(p)
    return palindromes