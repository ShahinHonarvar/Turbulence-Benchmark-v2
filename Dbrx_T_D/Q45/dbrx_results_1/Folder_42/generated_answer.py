def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(6, 10):
        for j in range(i, 10):
            substring = s[i:j + 1]
            if set(substring).issubset(english_letters):
                substring = substring.lower()
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes