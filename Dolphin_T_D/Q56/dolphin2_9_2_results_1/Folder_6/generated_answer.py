def all_substring_of_size_n(s):
    if len(s) < 23:
        return []
    res = set()
    for i in range(0, len(s) - 22):
        subs = s[i:i + 23]
        if len(set(subs)) == 23:
            res.add(subs)
    return list(res)