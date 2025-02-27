def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 119):
        t = s[i:i + 120]
        if len(set(t)) == 120:
            res.append(t)
    return res