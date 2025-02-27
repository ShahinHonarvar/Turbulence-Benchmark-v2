def all_substring_of_size_n(s):
    if len(s) < 93:
        return []
    res = set()
    for i in range(len(s) - 92):
        sub = s[i:i + 93]
        if len(set(sub)) == 93:
            res.add(sub)
    return list(res)