def palindromes_of_specific_lengths(input_string):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(30, 96):
        for j in range(34, 56):
            if i + j - 1 <= 95:
                substring = input_string[i - 1:i + j - 1].lower()
                if english_letters.issuperset(substring):
                    if substring == substring[::-1]:
                        palindromes.add(substring)
    return palindromes