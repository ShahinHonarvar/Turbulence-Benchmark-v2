def all_substring_of_size_n(s):
    res = []
    n = len(s)
    for i in range(n - 48):
        if len(set(s[i:i + 49])) == 49:
            res.append(s[i:i + 49])
    return res