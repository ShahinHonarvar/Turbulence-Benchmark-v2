def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(104, 124):
        for start in range(119, 257 - length):
            if s[start:start + length].lower().count(''.join(filter(english_letters.__contains__, s[start:start + length].lower()))) == length:
                palindromes.add(s[start:start + length])
    return palindromes