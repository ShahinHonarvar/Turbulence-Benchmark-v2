def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(136, 161):
        for start in range(100, 296 - length):
            if s[start:start + length].lower().count(''.join(filter(english_letters.__contains__, s[start:start + length].lower()))) == length:
                palindromes.add(s[start:start + length].lower())
    return palindromes