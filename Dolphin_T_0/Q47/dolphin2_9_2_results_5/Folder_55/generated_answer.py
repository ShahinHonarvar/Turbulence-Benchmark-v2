def palindromes_of_specific_lengths(s):
    s = s[10:76]
    palindromes = set()
    for length in range(10, 21):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if substring == substring[::-1] and all((c.isalpha() for c in substring)):
                palindromes.add(substring.lower())
    return palindromes