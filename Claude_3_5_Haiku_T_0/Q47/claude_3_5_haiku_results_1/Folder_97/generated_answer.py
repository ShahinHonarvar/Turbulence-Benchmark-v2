def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[28:95]
    for length in range(38, 50):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if candidate.isalpha() and candidate.lower() == candidate.lower()[::-1]:
                palindromes.add(candidate)
    return palindromes