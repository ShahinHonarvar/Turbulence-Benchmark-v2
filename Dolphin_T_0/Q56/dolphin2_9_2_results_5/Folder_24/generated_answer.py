def all_substring_of_size_n(s):
    if len(s) < 52:
        return []
    res = set()
    for i in range(len(s) - 51):
        if len(set(s[i:i + 52])) == 52:
            res.add(s[i:i + 52])
    return list(res)