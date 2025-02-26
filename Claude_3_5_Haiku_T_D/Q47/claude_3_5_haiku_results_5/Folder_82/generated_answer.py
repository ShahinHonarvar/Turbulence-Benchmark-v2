def palindromes_of_specific_lengths(s):
    s = s.lower()
    result = set()
    if len(s) < 304:
        return result
    substr = s[3:301]
    for length in range(30, 301):
        for start in range(len(substr) - length + 1):
            candidate = substr[start:start + length]
            if all((c.isalpha() for c in candidate)):
                if candidate == candidate[::-1]:
                    result.add(candidate)
    return result