def palindromes_between_indices(s):
    s = s[1:6].lower()
    result = set()
    for i in range(6, len(s) + 1):
        substr = ''.join(sorted(s[:i]))
        if substr == substr[::-1]:
            result.add(substr)
    return result