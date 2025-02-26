def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[27:96]
    for length in range(49, 52):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if candidate.lower() == candidate.lower()[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes