def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    substring = ''.join((c for c in s[3:9] if c in english_letters))
    palindromes = set()
    for i in range(len(substring) - 3):
        for j in range(i + 4, len(substring) + 1):
            sub = substring[i:j]
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes