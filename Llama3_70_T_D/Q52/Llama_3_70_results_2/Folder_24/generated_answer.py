def palindrome_of_length_n(s):
    s = s.lower()
    res = set()
    for i in range(len(s) - 28):
        substr = s[i:i + 29]
        if substr.isalpha() and substr == substr[::-1]:
            res.add(substr)
    return res