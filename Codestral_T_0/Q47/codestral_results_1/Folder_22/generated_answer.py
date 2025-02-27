def palindromes_of_specific_lengths(s):
    s = s[100:201]
    s = ''.join((c for c in s if c.isalpha()))
    s = s.lower()
    palindromes = set()
    for length in range(5, 11):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes