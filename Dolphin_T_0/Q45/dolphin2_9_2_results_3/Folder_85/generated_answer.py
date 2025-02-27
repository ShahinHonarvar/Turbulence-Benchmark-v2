def palindromes_between_indices(s):
    s = s[2:9]
    result = set()
    if len(s) < 7:
        return result
    for length in range(7, len(s) + 1):
        for start in range(0, len(s) - length + 1):
            if s[start:start + length] == s[start:start + length][::-1]:
                result.add(s[start:start + length].lower())
    return result