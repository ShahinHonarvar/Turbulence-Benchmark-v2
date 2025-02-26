def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s.lower()
    for length in range(35, 42):
        for start in range(32, 80 - length + 1):
            substring = s[start:start + length]
            if all((c.isalpha() for c in substring)):
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes