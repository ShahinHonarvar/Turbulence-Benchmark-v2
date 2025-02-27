def all_substring_of_size_n(s):
    if len(s) < 33:
        return []
    res = set()
    for i in range(len(s) - 32):
        sub = s[i:i + 33]
        if len(set(sub)) == len(sub):
            res.add(sub)
    return list(res)