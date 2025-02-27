def palindromes_of_specific_lengths(s):
    s = s[13:96]
    s_cleaned = ''.join((c.lower() for c in s if c.isalpha()))
    palindromes = set()
    for length in range(57, 61):
        for start in range(len(s_cleaned) - length + 1):
            substring = s_cleaned[start:start + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes