def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s.lower()
    for length in range(136, 152):
        for start in range(106, 281 - length + 1):
            substring = s[start:start + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes