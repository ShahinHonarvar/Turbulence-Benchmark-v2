def palindrome_of_length_at_least_n(s):
    s = s.lower()
    res = set()
    for i in range(len(s)):
        for j in range(i + 3, len(s)):
            substr = s[i:j + 1]
            if substr == substr[::-1] and len(substr) >= 40:
                res.add(substr)
    return res