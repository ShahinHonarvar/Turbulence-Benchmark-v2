def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[75:96]
    for length in range(7, 10):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if candidate.isalpha() and candidate.lower() == candidate.lower()[::-1]:
                palindromes.add(candidate)
    return palindromes