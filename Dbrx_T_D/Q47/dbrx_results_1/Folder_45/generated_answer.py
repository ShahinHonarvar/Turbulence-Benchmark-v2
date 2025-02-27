def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(3, 61):
        for i in range(70, 141 - length):
            candidate = s[i:i + length]
            if set(candidate) <= english_letters and candidate == candidate[::-1]:
                palindromes.add(candidate.lower())
    return palindromes