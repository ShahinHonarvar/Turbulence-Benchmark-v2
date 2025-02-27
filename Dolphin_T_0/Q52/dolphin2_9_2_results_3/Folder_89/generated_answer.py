def palindrome_of_length_n(s):
    n = 37
    res = set()
    s = ''.join(filter(str.isalpha, s.lower()))
    for i in range(len(s) - n + 1):
        if s[i:i + n] == s[i:i + n][::-1]:
            res.add(s[i:i + n])
    return res