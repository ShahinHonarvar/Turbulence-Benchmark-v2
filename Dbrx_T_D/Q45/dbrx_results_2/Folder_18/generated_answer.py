def palindromes_between_indices(s):
    palindromes = set()
    for i in range(1, min(7, len(s) - 1)):
        for j in range(i, min(7, len(s))):
            substring = s[i:j + 1].lower()
            if len(substring) < 3:
                continue
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes