def palindromes_of_specific_lengths(s):
    s = s[3:301]
    s = ''.join((c.lower() for c in s if c.isalpha()))
    n = len(s)
    palindromes = set()
    for length in range(30, 301):
        for i in range(n - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes