def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(18, 74):
        for i in range(15, 95 - length + 1):
            substring = s[i:i + length]
            if all((char in english_letters for char in substring)) and substring.lower() == substring.lower()[::-1]:
                palindromes.add(substring)
    return palindromes