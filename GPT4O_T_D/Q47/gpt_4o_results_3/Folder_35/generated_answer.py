def palindromes_of_specific_lengths(s):
    s = ''.join([c for c in s[34:91] if c.isalpha()]).lower()
    palindromes = set()
    for length in range(14, 40):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes