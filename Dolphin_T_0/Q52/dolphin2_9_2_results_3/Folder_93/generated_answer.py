def palindrome_of_length_n(s):
    s = s.lower()
    result = set([])
    for i in range(len(s) - 44):
        substr = s[i:i + 45]
        if substr == substr[::-1] and all((c.isalpha() for c in substr)):
            result.add(substr)
    return result