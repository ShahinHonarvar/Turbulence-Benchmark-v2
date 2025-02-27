def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[1:8]
    normalized = ''.join((c.lower() for c in substring if c.isalpha()))
    n = len(normalized)
    for length in range(3, 5):
        for i in range(n - length + 1):
            candidate = normalized[i:i + length]
            if candidate == candidate[::-1]:
                result.add(candidate)
    return result