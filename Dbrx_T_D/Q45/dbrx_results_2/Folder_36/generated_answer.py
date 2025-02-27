def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    s = ''.join((c.lower() for c in s if c in english_letters))
    if len(s) < 5:
        return palindromes
    for i in range(5, 9):
        for j in range(i, 9):
            substring = s[i:j + 1]
            if len(substring) >= 3 and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes