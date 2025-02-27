def palindromes_of_specific_lengths(s):
    s = s[43:96]
    result = set()
    for length in range(18, 48):
        for i in range(len(s) - length + 1):
            substr = s[i:i + length]
            if substr == substr[::-1] and substr.isalpha():
                result.add(substr.lower())
    return result