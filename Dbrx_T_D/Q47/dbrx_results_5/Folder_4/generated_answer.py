def palindromes_of_specific_lengths(s):
    valid_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(17, 67):
        for i in range(12, 93 - length + 1):
            substring = s[i:i + length]
            if all((char in valid_chars for char in substring)):
                if substring.lower() == substring.lower()[::-1]:
                    palindromes.add(substring)
    return palindromes