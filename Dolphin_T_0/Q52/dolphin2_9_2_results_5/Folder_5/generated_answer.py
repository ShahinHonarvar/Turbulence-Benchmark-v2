def palindrome_of_length_n(s):
    s = s.lower()
    res = set()
    for i in range(len(s) - 16):
        substr = s[i:i + 17]
        if all((c.isalpha() for c in substr)):
            if substr == substr[::-1]:
                res.add(substr)
    return res