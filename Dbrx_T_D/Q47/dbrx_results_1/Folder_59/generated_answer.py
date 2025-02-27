def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(3, 16):
        for index in range(100 - length + 1):
            substring = s[index:index + length]
            if len(english_letters & set(substring)) == len(substring):
                if substring == substring[::-1]:
                    palindromes.add(substring.lower())
    return palindromes