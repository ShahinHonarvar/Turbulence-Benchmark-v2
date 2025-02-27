def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(36, 43):
        for start in range(20, 75 - length + 1):
            substring = s[start:start + length]
            if len(english_letters & set(substring)) == len(substring):
                palindromes.add(substring.lower() if substring.lower() == substring else substring.upper())
    return palindromes