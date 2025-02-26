def palindromes_of_specific_lengths(s):
    palindromes = set()
    for length in range(3, 5):
        for start in range(1, 8 - length + 1):
            substring = s[start:start + length]
            if substring.isalpha() and substring.lower() == substring.lower()[::-1]:
                palindromes.add(substring)
    return palindromes