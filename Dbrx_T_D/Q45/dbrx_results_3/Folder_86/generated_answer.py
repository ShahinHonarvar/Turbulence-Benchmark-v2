def palindromes_between_indices(s):
    palindromes = set()
    for i in range(6, 10):
        for j in range(i, 10):
            substring = s[i:j + 1].lower()
            if len(substring) >= 4 and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes