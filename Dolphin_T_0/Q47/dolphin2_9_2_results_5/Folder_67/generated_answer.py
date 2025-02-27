def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(99, 64, -1):
        for j in range(i + 26, min(i + 34, len(s)), 1):
            sub = s[i:j]
            sub = ''.join((c for c in sub if c.isalpha())).lower()
            if sub == sub[::-1] and 26 <= len(sub) <= 33:
                palindromes.add(sub)
    return palindromes