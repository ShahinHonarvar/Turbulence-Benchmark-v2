def palindrome_of_length_at_least_n(s):
    res = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            tmp = s[i:j + 1][::-1]
            if tmp.lower() == tmp and len(tmp) >= 138:
                res.add(tmp)
    return res