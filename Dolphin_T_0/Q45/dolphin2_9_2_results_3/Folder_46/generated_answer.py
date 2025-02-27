def palindromes_between_indices(s):
    palindromes = set()
    for i in range(6, len(s) + 1):
        for j in range(len(s) - i + 1):
            sub = s[j:j + i]
            if sub == sub[::-1]:
                palindromes.add(sub.lower())
    return palindromes