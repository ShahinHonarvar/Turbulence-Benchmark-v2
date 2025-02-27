def palindromes_of_specific_lengths(s):
    t = s[31:80]
    palindromes = set()
    for length in range(35, 42):
        for i in range(len(t) - length + 1):
            substring = t[i:i + length]
            if substring == substring[::-1] and all((c.isalpha() for c in substring)):
                palindromes.add(substring.lower())
    return palindromes