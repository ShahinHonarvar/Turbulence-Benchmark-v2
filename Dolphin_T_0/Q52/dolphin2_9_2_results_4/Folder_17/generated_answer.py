def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 288):
        substr = s[i:i + 289]
        if substr == substr[::-1] and all((c.isalpha() for c in substr)):
            result.add(substr)
    return result