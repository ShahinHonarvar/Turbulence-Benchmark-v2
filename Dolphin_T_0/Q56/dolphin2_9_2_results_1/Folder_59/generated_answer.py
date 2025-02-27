def all_substring_of_size_n(s):
    res = set()
    n = len(s)
    for i in range(n):
        for j in range(i + 77, n):
            if len(set(s[i:j + 1])) == 77:
                res.add(s[i:j + 1])
    return list(res)