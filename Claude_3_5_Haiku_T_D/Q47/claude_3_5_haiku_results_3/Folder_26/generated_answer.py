def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    substring = s[24:85]
    for length in range(21, 32):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes