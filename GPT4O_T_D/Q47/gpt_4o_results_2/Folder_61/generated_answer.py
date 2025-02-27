def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s[:31].lower()
    for length in range(20, 31):
        for start in range(31 - length + 1):
            substring = s[start:start + length]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes