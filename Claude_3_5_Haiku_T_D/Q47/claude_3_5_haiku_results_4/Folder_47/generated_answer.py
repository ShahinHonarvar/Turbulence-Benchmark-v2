def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[39:95].lower()
    for length in range(14, 53):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if candidate.isalpha() and candidate == candidate[::-1]:
                result.add(candidate)
    return result