def all_substring_of_size_n(s):
    n = len(s)
    res = set()
    for i in range(n - 41):
        if len(set(s[i:i + 42])) == 42:
            res.add(s[i:i + 42])
    return list(res)