def all_substring_of_size_n(s):
    res = set()
    for i in range(len(s) - 5):
        if len(set(s[i:i + 6])) == 6:
            res.add(s[i:i + 6])
    return list(res)