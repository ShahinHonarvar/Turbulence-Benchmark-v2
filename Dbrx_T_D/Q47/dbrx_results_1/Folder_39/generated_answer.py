def palindromes_of_specific_lengths(string):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(31, 92):
        for j in range(50, 54):
            if i + j <= 91:
                substring = string[i:i + j]
                if english_letters.issuperset(substring) and substring == substring[::-1]:
                    palindromes.add(substring.lower())
    return palindromes