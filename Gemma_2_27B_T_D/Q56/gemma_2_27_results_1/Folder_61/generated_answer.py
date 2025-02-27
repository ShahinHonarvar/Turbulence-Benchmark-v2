def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 38):
        sub = s[i:i + 39]
        if len(set(sub)) == 39:
            res.append(sub)
    return res