def palindromes_between_indices(s):
    letters = s[4:8].lower()
    palindromes = set()
    for i in range(4, len(s) - 1, 2):
        for p in permutations(letters, i):
            if ''.join(p) == ''.join(p[::-1]):
                palindromes.add(''.join(p))
    return palindromes