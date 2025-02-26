def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[35:89]
    for length in range(24, 34):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate.lower())
    return palindromes