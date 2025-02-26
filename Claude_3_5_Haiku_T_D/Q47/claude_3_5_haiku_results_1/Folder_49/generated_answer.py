def palindromes_of_specific_lengths(s):
    s = s.lower()
    palindromes = set()
    if len(s) < 111:
        return palindromes
    substring = s[10:101]
    for length in range(10, 51):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if len(candidate) == length and candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes