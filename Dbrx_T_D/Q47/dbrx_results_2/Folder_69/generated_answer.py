def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(11, 97):
        for j in range(45, 53):
            if i + j - 1 <= 96:
                substring = s[i:i + j]
                if substring and all((char in english_letters for char in substring)):
                    if substring == substring[::-1]:
                        palindromes.add(substring.lower())
    return palindromes