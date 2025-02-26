def palindromes_of_specific_lengths(s):
    if len(s) < 61:
        return set()
    substr = s[16:61].lower()
    palindromes = set()
    for length in range(16, 40):
        for start in range(len(substr) - length + 1):
            candidate = substr[start:start + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes