def palindromes_between_indices(s):
    s = s[3:10].lower()
    s = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for i in range(3, 8):
        for p in itertools.permutations(s, i):
            if p == p[::-1]:
                palindromes.add(''.join(p))
    return palindromes