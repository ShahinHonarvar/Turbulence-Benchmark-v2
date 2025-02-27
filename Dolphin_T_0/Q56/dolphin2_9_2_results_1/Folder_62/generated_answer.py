def all_substring_of_size_n(s):
    n = len(s)
    res = []
    for i in range(n - 31):
        sub = s[i:i + 32]
        if len(set(sub)) == 32:
            res.append(sub)
    return res