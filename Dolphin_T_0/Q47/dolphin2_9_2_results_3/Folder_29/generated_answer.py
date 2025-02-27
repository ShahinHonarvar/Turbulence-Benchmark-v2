def palindromes_of_specific_lengths(s):
    substring = s[15:95]
    result = set()
    for length in range(18, 74):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate.lower() == candidate.lower()[::-1]:
                result.add(candidate)
    return result