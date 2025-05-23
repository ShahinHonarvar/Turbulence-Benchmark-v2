def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(30, 301):
        for start in range(3, 301 - length):
            substring = s[start:start + length]
            if all((char in english_letters for char in substring)) and substring == substring[::-1]:
                palindromes.add(substring.lower())
    return palindromes