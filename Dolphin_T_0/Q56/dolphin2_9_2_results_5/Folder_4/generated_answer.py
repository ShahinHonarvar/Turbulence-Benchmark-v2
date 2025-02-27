def all_substring_of_size_n(s):
    res = set()
    n = len(s)
    for i in range(n - 40):
        sub = s[i:i + 41]
        if len(set(sub)) == len(sub):
            res.add(sub)
    return list(res)