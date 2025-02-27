def palindromes_between_indices(string):
    palindromes = set()
    substring = string[3:8].lower()
    for i in range(len(substring)):
        for j in range(i + 2, len(substring) + 1):
            sub = substring[i:j]
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes