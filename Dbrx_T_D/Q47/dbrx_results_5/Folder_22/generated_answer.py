def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for length in range(5, 11):
        for index in range(100, 200 - length + 1):
            substring = s[index:index + length]
            if english_letters.issuperset(substring[0]) and english_letters.issuperset(substring[-1]):
                if substring[0].lower() == substring[-1].lower() and substring[0] == substring[-1]:
                    if substring == substring[::-1]:
                        palindromes.add(substring)
    return palindromes