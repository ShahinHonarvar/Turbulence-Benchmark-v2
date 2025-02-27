def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(len(s) - 9):
        for length in range(3, 6):
            substring = s[i:i + length]
            if substring and all((let in english_letters for let in substring)) and (substring.lower() == substring.lower()[::-1]):
                palindromes.add(substring)
    return palindromes