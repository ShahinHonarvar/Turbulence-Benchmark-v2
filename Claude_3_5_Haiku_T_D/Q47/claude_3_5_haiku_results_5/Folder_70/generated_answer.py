def palindromes_of_specific_lengths(s):
    s = s.lower()
    result = set()
    substring = s[10:71]
    for length in range(24, 53):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                result.add(candidate)
    return result