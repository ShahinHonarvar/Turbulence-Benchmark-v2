def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for start in range(len(s) - 391):
        substr = s[start:start + 392]
        if substr == substr[::-1]:
            result.add(substr)
    return result