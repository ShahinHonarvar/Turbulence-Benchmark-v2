def palindromes_between_indices(s):
    if len(s) <= 7:
        return set()
    substring = s[1:8]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 2, len(substring) + 1):
            sub = substring[i:j]
            if sub == sub[::-1]:
                palindromes.add(sub.lower())
    return palindromes