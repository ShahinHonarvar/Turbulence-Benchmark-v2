def palindromes_between_indices(s):
    s = s[3:7]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 3, len(s) + 1):
            sub = s[i:j]
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes