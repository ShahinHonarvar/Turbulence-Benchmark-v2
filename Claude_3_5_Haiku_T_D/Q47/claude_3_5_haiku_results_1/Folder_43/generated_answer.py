def palindromes_of_specific_lengths(s):
    palindromes = set()
    substr = s[41:90]
    for length in range(23, 39):
        for start in range(len(substr) - length + 1):
            candidate = substr[start:start + length]
            if candidate.isalpha() and candidate.lower() == candidate.lower()[::-1]:
                palindromes.add(candidate)
    return palindromes