def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(2, 10):
        for j in range(i, 10):
            substring = s[i:j + 1]
            if len(substring) >= 7 and substring[0] in english_letters and (substring[-1] in english_letters):
                substring = substring.lower()
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes