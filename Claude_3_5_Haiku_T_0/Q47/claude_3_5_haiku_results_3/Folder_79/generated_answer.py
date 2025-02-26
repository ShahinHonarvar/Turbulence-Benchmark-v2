def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s.lower()
    for length in range(3, 5):
        for start in range(1, 10 - length + 1):
            substring = s[start:start + length]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes