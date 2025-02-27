def palindromes_of_specific_lengths(s):
    s_filtered = ''.join((c.lower() for c in s[21:63] if c.isalpha()))
    n = len(s_filtered)
    palindromes = set()
    for length in range(22, 34):
        for i in range(n - length + 1):
            substring = s_filtered[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes