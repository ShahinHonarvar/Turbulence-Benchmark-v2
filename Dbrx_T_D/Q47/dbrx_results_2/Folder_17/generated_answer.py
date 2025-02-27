def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(52, 56):
        for i in range(22, 96 - length + 1):
            substring = s[i:i + length]
            if set(substring) <= english_letters:
                if substring == substring[::-1]:
                    palindromes.add(substring.lower())
    return palindromes