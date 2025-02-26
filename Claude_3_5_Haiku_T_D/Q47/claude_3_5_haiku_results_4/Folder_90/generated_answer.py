def palindromes_of_specific_lengths(s):
    palindromes = set()
    if len(s) < 281:
        return palindromes
    substring = s[106:281]
    for length in range(136, 152):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if candidate.isalpha() and candidate == candidate[::-1]:
                palindromes.add(candidate.lower())
    return palindromes