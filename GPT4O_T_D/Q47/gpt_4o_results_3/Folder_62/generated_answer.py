def palindromes_of_specific_lengths(s):
    s = s[26:88]
    s = ''.join((c for c in s if c.isalpha()))
    s = s.lower()
    palindromes = set()
    for length in range(52, 57):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes