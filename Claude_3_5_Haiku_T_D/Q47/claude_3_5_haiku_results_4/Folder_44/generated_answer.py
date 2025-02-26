def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s.lower()
    for length in range(31, 52):
        for start in range(18, 99 - length + 1):
            substring = s[start:start + length]
            if substring == substring[::-1] and all((char.isalpha() for char in substring)):
                palindromes.add(substring)
    return palindromes