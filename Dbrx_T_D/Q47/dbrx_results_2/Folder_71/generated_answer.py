def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(18, 66):
        for j in range(23, 37):
            if i + j - 1 <= 65:
                substring = s[i:i + j]
                if len(set(substring) - english_letters) == 0 and substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes