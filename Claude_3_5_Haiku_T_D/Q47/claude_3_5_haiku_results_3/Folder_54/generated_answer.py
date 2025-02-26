def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    if len(s) < 78:
        return palindromes
    substring = s[27:78]
    for length in range(18, 20):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate.isalpha() and candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes