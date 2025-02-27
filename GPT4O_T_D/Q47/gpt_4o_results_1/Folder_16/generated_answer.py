def palindromes_of_specific_lengths(s):
    substr = s[15:87]
    substr = ''.join(filter(str.isalpha, substr)).lower()
    results = set()
    min_len, max_len = (51, 60)
    for start in range(len(substr) - min_len + 1):
        for length in range(min_len, min(max_len, len(substr) - start) + 1):
            candidate = substr[start:start + length]
            if candidate == candidate[::-1]:
                results.add(candidate)
    return results