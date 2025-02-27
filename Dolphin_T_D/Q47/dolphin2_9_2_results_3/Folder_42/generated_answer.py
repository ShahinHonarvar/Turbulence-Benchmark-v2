def palindromes_of_specific_lengths(s):
    s = s[43:96].lower()
    result = set()
    for length in range(18, 48):
        for start in range(0, 96 - length + 1):
            substr = s[start:start + length]
            if substr == substr[::-1]:
                result.add(substr)
    return result