def palindromes_of_specific_lengths(s):
    if len(s) < 86:
        return set()
    substring = s[33:86].lower()
    result = set()
    for length in range(26, 32):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                result.add(candidate)
    return result