def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(155, 284):
        for length in range(104, 121):
            if i + length - 1 < len(s):
                substring = s[i:i + length]
                if substring.lower().isalpha() and all((char in english_letters for char in substring)) and (substring == substring[::-1]):
                    palindromes.add(substring)
    return palindromes