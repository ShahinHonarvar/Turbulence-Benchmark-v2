def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[36:93].lower()
    for length in range(10, 36):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if len(candidate) == length and candidate == candidate[::-1] and candidate.isalpha():
                result.add(candidate)
    return result