def palindromes_of_specific_lengths(s):
    result = set()
    if len(s) < 284:
        return result
    substring = s[155:284]
    for length in range(104, 121):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if candidate.lower() == candidate.lower()[::-1] and candidate.isalpha():
                result.add(candidate)
    return result