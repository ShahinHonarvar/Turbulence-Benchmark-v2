def palindromes_between_indices(s):
    indices = s[1:8]
    palindromes = set()
    for i in range(len(indices)):
        for j in range(i + 2, len(indices) + 1):
            substring = indices[i:j]
            if len(substring) >= 4 and substring == substring[::-1]:
                palindromes.add(substring.lower())
    return palindromes