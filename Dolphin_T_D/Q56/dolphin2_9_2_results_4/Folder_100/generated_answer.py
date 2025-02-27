def all_substring_of_size_n(s):
    n = len(s)
    m = 92
    res = set()
    for i in range(n - m + 1):
        if len(set(s[i:i + m])) == m:
            res.add(s[i:i + m])
    return list(res)