def palindromes_of_specific_lengths(s: str):
    s_filtered = ''.join((c for c in s[39:95] if c.isalpha())).lower()
    result = set()
    for length in range(14, 53):
        for start in range(len(s_filtered) - length + 1):
            substr = s_filtered[start:start + length]
            if substr == substr[::-1]:
                result.add(substr)
    return result