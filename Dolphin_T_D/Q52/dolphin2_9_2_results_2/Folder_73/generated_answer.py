def palindrome_of_length_n(s):
    s = s.lower()
    res = set()
    for i in range(len(s) - 40):
        tmp = s[i:i + 41]
        if tmp == tmp[::-1] and tmp.isalpha():
            res.add(tmp)
    return res