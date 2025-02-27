def palindromes_between_indices(s):
    palindromes = set()
    substring = s[4:8].lower()
    for i in range(len(substring)):
        for j in range(i + 3, len(substring) + 1):
            sub = substring[i:j]
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes