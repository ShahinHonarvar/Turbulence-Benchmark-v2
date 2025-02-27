def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(13, 50):
        for index in range(17, 96):
            substring = s[index:index + length]
            if all((char in english_letters for char in substring)):
                if substring.lower() == substring.lower()[::-1]:
                    palindromes.add(substring)
    return palindromes