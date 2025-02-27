def palindromes_of_specific_lengths(s):
    s = s[24:85]
    palindromes = set()
    for length in range(21, 32):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1] and all((c.isalpha() for c in substring)):
                palindromes.add(substring.lower())
    return palindromes