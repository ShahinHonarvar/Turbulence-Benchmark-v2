def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(24, 53):
        for start in range(10, 71 - length):
            substring = s[start:start + length]
            if english_letters.issuperset(substring) and substring == substring[::-1]:
                palindromes.add(substring.lower())
    return palindromes