def palindromes_of_specific_lengths(s):
    result = set()
    s = s.lower()
    substring = s[2:9]
    for start in range(len(substring)):
        for length in range(3, 5):
            if start + length > len(substring):
                break
            candidate = substring[start:start + length]
            if candidate.isalpha() and candidate == candidate[::-1]:
                result.add(candidate)
    return result