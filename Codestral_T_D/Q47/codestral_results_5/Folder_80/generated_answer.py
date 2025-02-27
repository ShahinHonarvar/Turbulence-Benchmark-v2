def palindromes_of_specific_lengths(s):
    result = set()
    s = s[35:89]
    for length in range(24, 34):
        for start in range(0, len(s) - length + 1):
            sub = s[start:start + length]
            if sub.isalpha() and sub.lower() == sub.lower()[::-1]:
                result.add(sub)
    return result