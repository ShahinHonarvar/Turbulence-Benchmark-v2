def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[18:66].lower()
    for length in range(23, 37):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                result.add(candidate)
    return result