def palindrome_of_length_n(s):
    s = s.lower()
    res = set()
    for i in range(len(s) - 115):
        if s[i:i + 116] == s[i:i + 116][::-1]:
            res.add(s[i:i + 116])
    return res