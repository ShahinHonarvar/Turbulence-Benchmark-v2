def palindrome_of_length_n(s):
    s = s.lower()
    res = set()
    for i in range(len(s) - 32):
        if s[i:i + 33] == s[i:i + 33][::-1]:
            res.add(s[i:i + 33])
    return res