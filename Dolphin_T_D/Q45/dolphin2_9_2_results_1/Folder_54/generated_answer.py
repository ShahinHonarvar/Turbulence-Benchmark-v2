def palindromes_between_indices(string):
    substring = string[4:10]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 3, len(substring)):
            sub = substring[i:j + 1]
            if sub == sub[::-1]:
                palindromes.add(sub.lower())
    return palindromes