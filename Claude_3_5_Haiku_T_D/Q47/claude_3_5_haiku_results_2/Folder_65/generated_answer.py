def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    for length in range(20, 67):
        for start in range(15, 96 - length + 1):
            substring = s[start:start + length]
            if all((char.isalpha() for char in substring)):
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes