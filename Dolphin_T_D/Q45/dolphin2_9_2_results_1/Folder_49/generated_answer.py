def palindromes_between_indices(s):
    palindromes = set()
    for i in range(5, 8):
        for j in range(i + 1, 8):
            for k in range(j + 1, 9):
                substring = s[i:j + 1] + s[k]
                if len(substring) >= 3 and substring == substring[::-1].lower():
                    palindromes.add(substring.lower())
    return palindromes