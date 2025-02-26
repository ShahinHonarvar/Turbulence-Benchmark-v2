def palindromes_of_specific_lengths(s):
    if len(s) < 201:
        return set()
    substr = s[100:201].lower()
    palindromes = set()
    for length in range(5, 11):
        for start in range(len(substr) - length + 1):
            candidate = substr[start:start + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes