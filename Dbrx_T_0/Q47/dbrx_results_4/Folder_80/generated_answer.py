def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(24, 34):
        for start in range(35, 89 - length + 1):
            substring = s[start:start + length]
            if all((char in english_letters for char in substring)):
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes