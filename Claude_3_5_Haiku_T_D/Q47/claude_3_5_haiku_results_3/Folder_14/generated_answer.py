def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    for length in range(6, 9):
        for start in range(10, 75 - length + 1):
            substring = s[start:start + length]
            if all((char.isalpha() for char in substring)):
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes