def palindromes_of_specific_lengths(s):
    if len(s) < 90:
        return set()
    substring = s[41:90]
    palindromes = set()
    for length in range(23, 39):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if candidate.lower() == candidate.lower()[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes