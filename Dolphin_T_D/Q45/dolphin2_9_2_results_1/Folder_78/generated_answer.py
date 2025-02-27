def palindromes_between_indices(string):
    substring = string[5:9]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 2, len(substring) + 1):
            sub = substring[i:j]
            if sub == sub[::-1] and len(sub) >= 3:
                palindromes.add(sub.lower())
    return palindromes