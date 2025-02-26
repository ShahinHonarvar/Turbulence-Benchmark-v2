def palindromes_of_specific_lengths(s):
    valid_palindromes = set()
    if len(s) <= 84:
        return valid_palindromes
    substring = s[30:85]
    for length in range(12, 21):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if candidate.isalpha() and candidate.lower() == candidate.lower()[::-1]:
                valid_palindromes.add(candidate)
    return valid_palindromes