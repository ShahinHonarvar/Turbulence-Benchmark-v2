def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s.lower()
    for length in range(45, 52):
        for start in range(40, 95 - length + 1):
            substring = s[start:start + length]
            if all((char.isalpha() for char in substring)):
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes