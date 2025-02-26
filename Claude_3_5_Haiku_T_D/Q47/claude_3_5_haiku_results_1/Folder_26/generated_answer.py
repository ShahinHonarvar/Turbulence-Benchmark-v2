def palindromes_of_specific_lengths(s):
    substring = s[24:85].lower()
    result = set()
    for length in range(21, 32):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if len(candidate) == length and candidate == candidate[::-1] and candidate.isalpha():
                result.add(candidate)
    return result