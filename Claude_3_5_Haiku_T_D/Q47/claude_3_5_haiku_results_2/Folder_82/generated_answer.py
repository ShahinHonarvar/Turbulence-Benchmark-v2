def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    for length in range(30, 301):
        for start in range(3, 301 - length + 1):
            substring = s[start:start + length]
            if len(substring) == length and all((char.isalpha() for char in substring)):
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes