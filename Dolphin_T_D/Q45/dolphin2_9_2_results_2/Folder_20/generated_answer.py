def palindromes_between_indices(s):
    substring = s[2:9]
    palindromes = set()
    for i in range(4, len(substring) + 1):
        for j in range(len(substring) - i + 1):
            sub = substring[j:j + i]
            if sub == sub[::-1]:
                palindromes.add(sub.lower())
    return palindromes