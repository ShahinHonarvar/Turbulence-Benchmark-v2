def palindromes_of_specific_lengths(s):
    result = set()
    substr = s[26:88].lower()
    for length in range(52, 57):
        for start in range(len(substr) - length + 1):
            candidate = substr[start:start + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                result.add(candidate)
    return result