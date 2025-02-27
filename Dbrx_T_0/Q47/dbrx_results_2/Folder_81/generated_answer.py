def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(12, 221):
        for start in range(12, len(s) - length + 1):
            substring = s[start:start + length]
            if set(substring) <= english_letters and substring == substring[::-1]:
                palindromes.add(substring.lower())
    return palindromes