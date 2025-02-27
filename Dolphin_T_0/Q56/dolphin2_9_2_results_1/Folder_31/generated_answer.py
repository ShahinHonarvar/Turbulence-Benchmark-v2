def all_substring_of_size_n(s):
    if len(s) < 46:
        return []
    res = []
    for i in range(len(s) - 45):
        if len(set(s[i:i + 46])) == 46:
            res.append(s[i:i + 46])
    return list(set(res))