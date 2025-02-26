def palindromes_of_specific_lengths(s):
    if len(s) < 91:
        return set()
    substring = s[26:91]
    palindromes = set()
    for length in range(27, 59):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate.lower())
    return palindromes