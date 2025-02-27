def all_substring_of_size_n(s):
    res = set()
    for i in range(len(s) - 23):
        res.add(s[i:i + 24])
    return list(res)