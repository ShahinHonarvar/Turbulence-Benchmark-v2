def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[27:78]
    for start in range(len(substring)):
        for length in range(18, 20):
            if start + length > len(substring):
                break
            candidate = substring[start:start + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                result.add(candidate.lower())
    return result