def all_substring_of_size_n(s):
    n = 38
    res = []
    for i in range(len(s)):
        temp = s[i:i + n]
        if len(temp) == n and len(set(temp)) == n:
            res.append(temp)
    return res