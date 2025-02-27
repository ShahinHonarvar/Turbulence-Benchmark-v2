def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(155, 284):
        for length in range(104, 121):
            if i + length - 1 < len(s):
                substring = s[i:i + length]
                if substring == substring[::-1] and all((char in english_letters for char in substring)):
                    palindromes.add(substring)
    return palindromes