def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(100, 170):
        for i in range(103, 277 - length):
            substring = s[i:i + length]
            if all((char in english_letters for char in substring)) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes