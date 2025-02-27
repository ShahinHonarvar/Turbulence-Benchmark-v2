def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(124, 284):
        for length in range(115, 135):
            if i + length <= 283:
                substring = s[i:i + length]
                if substring and all((char in english_letters for char in substring)) and (substring == substring[::-1]):
                    palindromes.add(substring)
    return palindromes