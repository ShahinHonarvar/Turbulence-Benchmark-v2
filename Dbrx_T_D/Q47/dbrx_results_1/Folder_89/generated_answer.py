def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(18, 89):
        for length in range(12, 15):
            if i + length <= 89:
                substring = s[i:i + length]
                if substring.lower() == substring.lower()[::-1] and all((char in english_letters for char in substring)):
                    palindromes.add(substring)
    return palindromes