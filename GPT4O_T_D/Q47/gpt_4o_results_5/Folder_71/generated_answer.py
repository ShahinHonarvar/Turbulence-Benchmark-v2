def palindromes_of_specific_lengths(s):
    substr = s[18:66]
    palindromes = set()
    normalized_substr = ''.join(filter(str.isalpha, substr)).lower()
    n = len(normalized_substr)
    for start in range(n):
        for length in range(23, 37):
            end = start + length
            if end <= n:
                candidate = normalized_substr[start:end]
                if candidate == candidate[::-1]:
                    palindromes.add(substr[start:end])
    return palindromes