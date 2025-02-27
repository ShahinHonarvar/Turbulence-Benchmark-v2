def all_substring_of_size_n(s):
    if len(set(s)) < 52:
        return []
    res = []
    for i in range(len(s) - 51):
        if len(set(s[i:i + 52])) == 52:
            res.append(s[i:i + 52])
    return res