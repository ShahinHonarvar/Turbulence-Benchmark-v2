def palindromes_of_specific_lengths(s):
    s = ''.join((c.lower() for c in s[23:95] if c.isalpha()))
    palindromes = set()
    n = len(s)
    for length in range(17, 56):
        for i in range(n - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes