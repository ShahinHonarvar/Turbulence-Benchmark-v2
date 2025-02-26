def palindromes_of_specific_lengths(s):
    result = set()
    s = s.lower()
    substring = s[32:80]
    for length in range(35, 42):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if len(candidate) == length and candidate == candidate[::-1] and candidate.isalpha():
                result.add(candidate)
    return result