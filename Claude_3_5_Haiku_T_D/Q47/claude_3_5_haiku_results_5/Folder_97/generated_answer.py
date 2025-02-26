def palindromes_of_specific_lengths(s):
    result = set()
    if len(s) <= 94:
        return result
    substring = s[28:95].lower()
    for length in range(38, 50):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if len(candidate) == length and candidate == candidate[::-1] and candidate.isalpha():
                result.add(candidate)
    return result