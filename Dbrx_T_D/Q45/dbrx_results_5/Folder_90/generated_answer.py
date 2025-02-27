def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    substr = set(s[0:6])
    palindromes = set()
    for i in range(4, 7):
        for combo in itertools.combinations_with_replacement(substr, i):
            candidate = ''.join(combo)
            if candidate in english_letters and candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes