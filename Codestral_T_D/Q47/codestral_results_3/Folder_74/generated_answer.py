def palindromes_of_specific_lengths(s):
    s = s[30:85]
    s = s.lower()
    s = ''.join((c for c in s if c.isalpha()))
    palindromes = set()
    for l in range(12, 21):
        for i in range(len(s) - l + 1):
            sub = s[i:i + l]
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes