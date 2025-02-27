def palindromes_of_specific_lengths(string):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(27, 78):
        for j in range(i - 18, i - 9):
            substring = string[j:i]
            if english_letters.issuperset(substring):
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes