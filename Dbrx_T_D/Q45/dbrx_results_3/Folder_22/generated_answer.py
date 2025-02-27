def palindromes_between_indices(s):
    palindromes = set()
    for i in range(5, 7):
        for j in range(i, 7):
            substring = s[i:j + 1].lower()
            if len(substring) >= 3 and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes