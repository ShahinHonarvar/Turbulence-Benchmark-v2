def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    if len(s) < 7 or s[5:7].isalpha() == False:
        return palindromes
    for i in range(5, 7):
        for j in range(i, 7):
            substring = s[i:j + 1]
            if set(substring).issubset(english_letters) and len(substring) >= 5:
                palindromes.add(''.join(sorted(substring, key=str.lower)))
    return palindromes