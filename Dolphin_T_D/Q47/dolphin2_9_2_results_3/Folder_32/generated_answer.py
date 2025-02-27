def palindromes_of_specific_lengths(s):
    palindromes = set()
    for length in range(43, 48):
        for i in range(16, 78 - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1] and all((c.isalpha() for c in substring)):
                palindromes.add(substring.lower())
    return palindromes