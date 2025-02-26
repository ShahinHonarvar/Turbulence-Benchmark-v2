def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[40:95]
    for length in range(45, 52):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if candidate.isalpha() and candidate.lower() == candidate.lower()[::-1]:
                palindromes.add(candidate)
    return palindromes