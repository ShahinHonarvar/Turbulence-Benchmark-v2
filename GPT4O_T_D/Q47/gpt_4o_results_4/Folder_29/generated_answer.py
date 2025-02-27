def palindromes_of_specific_lengths(s):
    s = s[15:95]
    alphanumeric_str = ''.join((c for c in s if c.isalpha())).lower()
    palindromes = set()
    for length in range(18, 74):
        for start in range(len(alphanumeric_str) - length + 1):
            substring = alphanumeric_str[start:start + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes