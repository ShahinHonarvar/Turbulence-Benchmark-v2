def palindromes_between_indices(s):
    if not 6 <= 9 < len(s):
        return set()
    substring = s[6:10]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 2, len(substring) + 1):
            sub = substring[i:j]
            if sub == sub[::-1]:
                palindromes.add(sub.lower())
    return palindromes