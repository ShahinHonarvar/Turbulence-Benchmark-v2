def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[12:123]
    substring = ''.join((c.lower() for c in substring if c.isalpha()))
    n = len(substring)
    for length in range(12, 221):
        for i in range(n - length + 1):
            substr = substring[i:i + length]
            if substr == substr[::-1]:
                result.add(substr)
    return result