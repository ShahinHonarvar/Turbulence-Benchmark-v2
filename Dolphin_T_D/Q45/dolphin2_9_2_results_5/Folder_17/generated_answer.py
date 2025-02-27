def palindromes_between_indices(string):
    letters = set(''.join(string[2:7]))
    palindromes = set()
    for i in range(4, len(string[2:7]) + 1):
        for j in itertools.combinations(letters, i):
            if j == j[::-1]:
                palindromes.add(''.join(j).lower())
    return palindromes if palindromes else None