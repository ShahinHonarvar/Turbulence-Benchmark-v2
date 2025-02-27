def palindromes_of_specific_lengths(s):
    valid_chars = [c for c in s[18:99] if c.isalpha()]
    lower_s = ''.join(valid_chars).lower()
    palindromes = set()
    for length in range(31, 52):
        for i in range(len(lower_s) - length + 1):
            substr = lower_s[i:i + length]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes