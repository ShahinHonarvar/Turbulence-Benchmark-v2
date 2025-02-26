def palindromes_of_specific_lengths(s):
    if len(s) <= 82:
        return set()
    substring = s[23:83]
    valid_palindromes = set()
    for start in range(len(substring)):
        for length in range(32, 35):
            if start + length > len(substring):
                break
            candidate = substring[start:start + length]
            if candidate.lower() == candidate.lower()[::-1] and candidate.isalpha():
                valid_palindromes.add(candidate)
    return valid_palindromes