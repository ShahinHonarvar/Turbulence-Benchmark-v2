def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(24, 85):
        for j in range(21, 32):
            substring = s[i:i + j]
            if len(substring) == j and all((char in english_letters for char in substring)):
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes