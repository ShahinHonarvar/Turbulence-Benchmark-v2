def all_substring_of_size_n(s):
    if len(s) < 70:
        return []
    res = []
    for i in range(len(s) - 70 + 1):
        sub = s[i:i + 70]
        if len(set(sub)) == 70:
            res.append(sub)
    return list(set(res))