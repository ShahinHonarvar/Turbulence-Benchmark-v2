def palindrome_of_length_n(s):
    s = s.lower()
    n = len(s)
    res = set()
    for i in range(n):
        for j in range(i + 9, n):
            if s[i:j + 1] == s[i:j + 1][::-1]:
                res.add(s[i:j + 1])
    return res