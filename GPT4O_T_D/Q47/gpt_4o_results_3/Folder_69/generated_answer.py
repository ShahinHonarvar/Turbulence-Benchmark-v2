def palindromes_of_specific_lengths(s):
    if len(s) < 97:
        return set()
    substr = s[11:97].lower()
    valid_palindromes = set()
    for length in range(45, 53):
        for start in range(0, len(substr) - length + 1):
            candidate = substr[start:start + length]
            if candidate.isalpha() and candidate == candidate[::-1]:
                valid_palindromes.add(candidate)
    return valid_palindromes