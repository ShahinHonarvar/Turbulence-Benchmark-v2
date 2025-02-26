def palindromes_of_specific_lengths(s):
    if len(s) < 91:
        return set()
    substring = s[34:91].lower()
    valid_palindromes = set()
    for length in range(14, 40):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if len(candidate) == length and candidate.isalpha() and (candidate == candidate[::-1]):
                valid_palindromes.add(candidate)
    return valid_palindromes