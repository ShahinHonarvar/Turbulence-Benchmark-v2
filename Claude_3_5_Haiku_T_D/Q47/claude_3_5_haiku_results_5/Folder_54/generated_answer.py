def palindromes_of_specific_lengths(s):
    if len(s) < 78:
        return set()
    substring = s[27:78]
    palindromes = set()
    for length in range(18, 20):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if candidate.isalpha() and candidate.lower() == candidate.lower()[::-1]:
                palindromes.add(candidate)
    return palindromes