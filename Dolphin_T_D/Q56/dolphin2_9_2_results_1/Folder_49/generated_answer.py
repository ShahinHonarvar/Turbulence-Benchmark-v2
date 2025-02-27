def all_substring_of_size_n(s):
    if len(set(s)) != len(s):
        return []
    subs = [s[i:i + 73] for i in range(len(s) - 72)]
    res = []
    for sub in subs:
        if len(set(sub)) == 73:
            res.append(sub)
    return res