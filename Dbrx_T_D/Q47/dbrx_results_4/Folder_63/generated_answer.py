def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(33, 86):
        for length in range(26, 32):
            substring = s[i:i + length]
            if substring.lower() == substring.lower()[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes