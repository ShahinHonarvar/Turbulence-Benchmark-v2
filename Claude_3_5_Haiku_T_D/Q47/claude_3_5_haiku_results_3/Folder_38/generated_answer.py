def palindromes_of_specific_lengths(s):
    results = set()
    s = s.lower()
    substring = s[18:88]
    for length in range(38, 61):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                results.add(candidate)
    return results