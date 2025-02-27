def palindromes_between_indices(s):
    string = s[2:9]
    string_lower = string.lower()
    palindromes = set()
    for i in range(6, len(string) + 1):
        for j in combinations(string_lower, i):
            word = ''.join(j)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes