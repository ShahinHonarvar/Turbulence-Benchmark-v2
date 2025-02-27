def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(12, 221):
        for i in range(12, len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1] and set(substring).issubset(english_letters):
                palindromes.add(substring.lower())
    return palindromes