def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[130:296]
    cleaned = ''.join((c.lower() for c in substring if c.isalpha()))
    n = len(cleaned)
    for length in range(103, 159):
        for i in range(n - length + 1):
            substr = cleaned[i:i + length]
            if substr == substr[::-1]:
                result.add(substr)
    return result