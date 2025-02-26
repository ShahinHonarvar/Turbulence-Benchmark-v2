def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    substring = s[12:123]
    for length in range(12, 221):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if len(candidate) == length and candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes