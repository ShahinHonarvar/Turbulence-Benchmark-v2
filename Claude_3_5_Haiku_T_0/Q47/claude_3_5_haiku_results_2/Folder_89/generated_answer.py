def palindromes_of_specific_lengths(s):
    palindromes = set()
    substring = s[18:89]
    for length in range(12, 15):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate.isalpha() and candidate.lower() == candidate.lower()[::-1]:
                palindromes.add(candidate)
    return palindromes