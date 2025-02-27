def palindromes_of_specific_lengths(s):
    s = s[119:257].lower()
    valid_chars = ''.join((c for c in s if c.isalpha()))
    palindromes = set()
    n = len(valid_chars)
    for length in range(104, 124):
        for i in range(n - length + 1):
            substring = valid_chars[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes