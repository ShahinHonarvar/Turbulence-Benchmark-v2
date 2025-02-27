def palindromes_of_specific_lengths(s):
    s = s.lower()
    substring = s[75:96]
    result = set()
    for length in range(7, 10):
        for i in range(len(substring) - length + 1):
            candidate = ''.join(filter(str.isalpha, substring[i:i + length]))
            if len(candidate) == length and candidate == candidate[::-1]:
                result.add(candidate)
    return result