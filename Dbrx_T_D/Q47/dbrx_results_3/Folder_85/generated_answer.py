def palindromes_of_specific_lengths(string):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(29, 99):
        for length in range(6, 10):
            if i + length <= 99:
                substring = string[i:i + length]
                if english_letters.issuperset(substring):
                    if substring == substring[::-1]:
                        palindromes.add(substring)
    return palindromes