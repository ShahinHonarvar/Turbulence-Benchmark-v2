def palindromes_of_specific_lengths(s):
    s = s[29:96 + 1]
    result = set()
    for length in range(12, 19):
        for i in range(len(s) - length + 1):
            substr = s[i:i + length]
            if all(('a' <= c.lower() <= 'z' for c in substr)) and substr.lower() == substr.lower()[::-1]:
                result.add(substr.lower())
    return result