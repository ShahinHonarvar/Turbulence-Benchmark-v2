def palindromes_of_specific_lengths(s):
    s = s[1:10]
    s_lower = ''.join(filter(str.isalpha, s.lower()))
    n = len(s_lower)
    palindromes = set()
    for length in range(3, 8):
        for start in range(n - length + 1):
            substr = s_lower[start:start + length]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes