def palindromes_of_specific_lengths(s):
    result = set()
    if len(s) < 95:
        return result
    substring = s[23:95].lower()
    for length in range(17, 56):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                result.add(candidate)
    return result