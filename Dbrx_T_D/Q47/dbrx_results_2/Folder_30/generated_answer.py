def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(14, 91):
        for j in range(i, 92):
            if len(s[i:j]) >= 55 and len(s[i:j]) <= 71:
                substring = ''.join(filter(english_letters.__contains__, s[i:j]))
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes