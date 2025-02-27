def palindromes_of_specific_lengths(s):
    s = ''.join((c for c in s if c.isalpha()))
    s = s[:50]
    palindromes = set()
    for length in range(50, 101):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub == sub[::-1]:
                palindromes.add(sub.lower())
    return palindromes