def palindromes_of_specific_lengths(s):
    palindromes = set()
    if len(s) < 89:
        return palindromes
    substring = s[62:89]
    for length in range(18, 22):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if candidate.isalpha() and candidate.lower() == candidate.lower()[::-1]:
                palindromes.add(candidate)
    return palindromes