def palindromes_between_indices(s):
    letters = set(s[0:3].lower())
    palindromes = set()
    for length in range(3, 100):
        for comb in itertools.combinations('abcdefghijklmnopqrstuvwxyz', length):
            comb = ''.join(comb)
            if letters.issuperset(comb):
                palindromes.add(comb)
                palindromes.add(comb[::-1])
    return palindromes