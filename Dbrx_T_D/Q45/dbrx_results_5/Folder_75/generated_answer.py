def palindromes_between_indices(s):
    letters = set(s[2:5].lower())
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for combo in itertools.combinations(letters, length):
            combo = ''.join(combo)
            if combo == combo[::-1]:
                palindromes.add(combo)
    return palindromes