def palindromes_of_specific_lengths(s):
    result = set()
    s = ''.join((c.lower() for c in s if c.isalpha()))
    for i in range(10, min(101, len(s))):
        for j in range(10, 51):
            if i + j <= len(s):
                substr = s[i:i + j]
                if substr == substr[::-1]:
                    result.add(substr)
    return result