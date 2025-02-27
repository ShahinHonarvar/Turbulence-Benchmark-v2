def palindrome_of_length_at_least_n(s):
    s = s.lower()
    res = set()
    for i in range(len(s) - 29):
        for j in range(i + 30, len(s) + 1):
            s_temp = s[i:j]
            if s_temp == s_temp[::-1]:
                res.add(s_temp)
    return res