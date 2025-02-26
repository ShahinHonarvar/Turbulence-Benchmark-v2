def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s.lower()
    for length in range(16, 40):
        for start in range(16, 61 - length):
            substring = s[start:start + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes