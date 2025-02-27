def all_substring_of_size_n(s):
    res = set()
    n = len(s)
    for i in range(n - 60):
        res.add(s[i:i + 61])
    return list(res)