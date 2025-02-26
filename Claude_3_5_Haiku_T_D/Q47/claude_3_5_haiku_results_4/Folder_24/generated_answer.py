def palindromes_of_specific_lengths(s):
    result = set()
    s = s.lower()
    for length in range(42, 78):
        for start in range(12, 93 - length + 1):
            substring = s[start:start + length]
            if all((c.isalpha() for c in substring)):
                if substring == substring[::-1]:
                    result.add(substring)
    return result