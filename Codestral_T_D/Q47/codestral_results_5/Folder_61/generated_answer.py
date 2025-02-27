def palindromes_of_specific_lengths(s):
    s = s[:31].lower()
    s = ''.join([c for c in s if c.isalpha()])
    palindromes = set()
    for length in range(20, 31):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes