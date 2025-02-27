def palindromes_between_indices(s):
    substring = s[5:7]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 2, len(substring) + 1):
            sub = substring[i:j]
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes