def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[65:100].lower()
    for length in range(26, 34):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                result.add(candidate)
    return result