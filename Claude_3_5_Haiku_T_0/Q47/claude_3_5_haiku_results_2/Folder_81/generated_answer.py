def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    for length in range(12, 221):
        for start in range(12, 123 - length + 1):
            substring = s[start:start + length]
            if all((char.isalpha() for char in substring)):
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes