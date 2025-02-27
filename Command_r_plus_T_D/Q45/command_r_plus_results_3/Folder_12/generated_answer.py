def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(3, 9):
        for j in range(i + 1, 9):
            substring = s[i:j]
            if set(substring).issubset(english_letters) and substring == substring[::-1] and (len(substring) >= 4):
                palindromes.add(substring)
    return palindromes