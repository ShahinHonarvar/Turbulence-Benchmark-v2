def all_substring_of_size_n(s):
    res = []
    if len(s) < 50:
        return res
    for i in range(len(s) - 49):
        if len(set(s[i:i + 50])) == 50:
            res.append(s[i:i + 50])
    return list(set(res))