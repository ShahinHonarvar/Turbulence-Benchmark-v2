def palindrome_of_length_n(s):
    s = s.lower()
    n = 445
    result = set()
    for i in range(len(s) - n + 1):
        substr = s[i:i + n]
        if substr == substr[::-1] and all((c.isalpha() for c in substr)):
            result.add(substr)
    return result