def palindromes_of_specific_lengths(s):
    s = s.lower()
    valid_range = ''.join([c for c in s[:6] if c.isalpha()])
    palindromes = set()
    for length in range(3, 6):
        for i in range(len(valid_range) - length + 1):
            substring = valid_range[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes