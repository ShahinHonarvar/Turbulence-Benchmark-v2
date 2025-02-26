def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s.lower()
    substr = s[65:100]
    for length in range(26, 34):
        for start in range(len(substr) - length + 1):
            candidate = substr[start:start + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes