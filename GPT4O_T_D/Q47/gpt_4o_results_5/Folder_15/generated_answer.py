def palindromes_of_specific_lengths(s):
    s = s[:7]
    valid_chars = [c.lower() for c in s if c.isalpha()]
    n = len(valid_chars)
    palindromes = set()
    for length in range(3, 7):
        for i in range(n - length + 1):
            substring = valid_chars[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(''.join(substring))
    return palindromes