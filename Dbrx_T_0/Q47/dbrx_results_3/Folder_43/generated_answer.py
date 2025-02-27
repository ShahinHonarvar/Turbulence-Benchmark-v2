def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(23, 39):
        for start in range(41, 90 - length + 1):
            substring = s[start:start + length]
            if all((char in english_letters for char in substring)):
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes