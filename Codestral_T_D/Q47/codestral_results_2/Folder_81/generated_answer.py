def palindromes_of_specific_lengths(s):
    s = s[12:123].lower()
    s = ''.join((c for c in s if c.isalpha()))
    palindromes = set()
    for i in range(12, 221):
        for j in range(len(s) - i + 1):
            sub = s[j:j + i]
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes