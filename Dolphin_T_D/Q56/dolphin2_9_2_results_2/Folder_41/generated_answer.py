def all_substring_of_size_n(s):
    res = []
    size = 74
    for i in range(len(s) - size + 1):
        sub = s[i:i + size]
        if len(set(sub)) == size:
            res.append(sub)
    return res