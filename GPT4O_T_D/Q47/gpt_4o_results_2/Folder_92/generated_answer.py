def palindromes_of_specific_lengths(s):
    s = s.lower()
    s = ''.join(filter(str.isalpha, s[:5]))
    results = set()
    n = len(s)
    for length in range(3, 5):
        for start in range(n - length + 1):
            substr = s[start:start + length]
            if substr == substr[::-1]:
                results.add(substr)
    return results