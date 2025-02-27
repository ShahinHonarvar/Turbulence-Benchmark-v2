def palindromes_of_specific_lengths(s):
    if len(s) < 89:
        return set()
    s = s[35:89]
    s = ''.join(filter(str.isalpha, s))
    s = s.lower()
    palindromes = set()
    for length in range(24, 34):
        for i in range(len(s) - length + 1):
            substr = s[i:i + length]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes