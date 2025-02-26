def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s.lower()
    for start in range(14, 91 - 55 + 1):
        for length in range(55, 72):
            substring = s[start:start + length]
            if len(substring) == length and all((char.isalpha() for char in substring)):
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes