def palindromes_between_indices(s):
    if len(s) < 8:
        return set()
    palindromes = set()
    for i in range(5, 8):
        for j in range(i + 2, len(s) + 1):
            substring = s[i:j]
            if len(substring) >= 3 and substring == substring[::-1]:
                palindromes.add(substring.lower())
    return palindromes