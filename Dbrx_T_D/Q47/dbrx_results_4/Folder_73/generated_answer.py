def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(22, 34):
        for start in range(21, 63 - length + 1):
            substring = s[start:start + length]
            if english_letters.issuperset(substring) and substring == substring[::-1]:
                palindromes.add(substring.lower())
    return palindromes