def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(16, 40):
        for start in range(16, 61 - length + 1):
            if s[start:start + length].lower().join(english_letters) == s[start:start + length].lower():
                palindromes.add(s[start:start + length])
    return palindromes