def palindrome_of_length_n(s):
    s = s.lower()
    l = len(s)
    res = set()
    for i in range(l):
        for j in range(i + 1, l + 1):
            if s[i:j][::-1] == s[i:j] and len(s[i:j]) == 90:
                res.add(s[i:j])
    return res