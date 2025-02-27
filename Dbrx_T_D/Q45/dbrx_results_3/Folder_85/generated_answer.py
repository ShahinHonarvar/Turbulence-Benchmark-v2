def palindromes_between_indices(s):
    letters = set(s[2:9].lower())
    palindromes = set()
    for length in range(7, 14):
        for combination in itertools.combinations(letters, length):
            candidate = ''.join(combination)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes