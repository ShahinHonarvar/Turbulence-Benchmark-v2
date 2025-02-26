def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s.lower()
    substring = s[13:96]
    for length in range(57, 61):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes