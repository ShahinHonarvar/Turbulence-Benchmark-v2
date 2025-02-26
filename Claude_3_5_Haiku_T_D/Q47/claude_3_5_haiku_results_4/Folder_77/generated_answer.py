def palindromes_of_specific_lengths(s):
    result = set()
    s = s.lower()
    substring = s[103:277]
    for length in range(100, 170):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                result.add(candidate)
    return result