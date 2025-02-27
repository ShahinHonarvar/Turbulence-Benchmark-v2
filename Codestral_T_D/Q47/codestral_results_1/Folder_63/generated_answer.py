def palindromes_of_specific_lengths(s):
    s = s[33:86]
    s = ''.join((c for c in s if c.isalpha()))
    s = s.lower()
    palindromes = set()
    for length in range(26, 32):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes