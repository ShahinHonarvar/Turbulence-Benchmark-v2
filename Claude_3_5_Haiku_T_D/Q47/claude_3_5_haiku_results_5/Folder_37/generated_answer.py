def palindromes_of_specific_lengths(s):
    palindromes = set()
    substr = s[:10].lower()
    for length in range(3, 6):
        for start in range(len(substr) - length + 1):
            candidate = substr[start:start + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes