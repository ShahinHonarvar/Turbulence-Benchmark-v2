def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s[200:301]
    for i in range(len(s)):
        for j in range(i + 10, min(len(s) + 1, i + 51)):
            sub = s[i:j]
            if sub == sub[::-1] and all((c.isalpha() for c in sub)):
                palindromes.add(sub.lower())
    return palindromes