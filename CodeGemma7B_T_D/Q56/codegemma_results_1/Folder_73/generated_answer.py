def all_substring_of_size_n(s):
    res = set()
    n = len(s)
    for i in range(n - 20 + 1):
        for j in range(i + 20):
            res.add(s[i:j + 1])
    return list(res)