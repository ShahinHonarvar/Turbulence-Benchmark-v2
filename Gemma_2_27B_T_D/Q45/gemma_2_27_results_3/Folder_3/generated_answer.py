def palindromes_between_indices(s):
    letters = s[7:10].lower()
    palindromes = set()
    for i in range(3, len(letters) + 1, 2):
        for permutation in itertools.permutations(letters):
            substring = ''.join(permutation[:i])
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes