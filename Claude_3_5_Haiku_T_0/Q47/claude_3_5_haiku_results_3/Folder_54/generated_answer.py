def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[27:78]
    for start in range(len(substring)):
        for length in range(18, 20):
            if start + length > len(substring):
                break
            candidate = substring[start:start + length]
            if candidate.isalpha() and candidate.lower() == candidate.lower()[::-1]:
                palindromes.add(candidate)
    return palindromes