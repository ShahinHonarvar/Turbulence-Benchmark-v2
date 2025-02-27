def palindromes_of_specific_lengths(s):
    palindromes = set()
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    for length in range(26, 32):
        for start in range(33, 86 - length + 1):
            if s[start:start + length].lower() in palindromes:
                continue
            if set(s[start:start + length]) <= english_letters:
                palindromes.add(s[start:start + length].lower())
    return palindromes