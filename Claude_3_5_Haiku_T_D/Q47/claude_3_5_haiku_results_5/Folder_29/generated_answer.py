def palindromes_of_specific_lengths(s):
    s = s.lower()
    substring = s[15:95]
    result = set()
    for length in range(18, 74):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                result.add(candidate)
    return result