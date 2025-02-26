def palindromes_of_specific_lengths(s):
    if len(s) < 96:
        return set()
    substr = s[75:96].lower()
    palindromes = set()
    for length in range(7, 10):
        for start in range(len(substr) - length + 1):
            candidate = substr[start:start + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes