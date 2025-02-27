def all_substring_of_size_n(s):
    length = len(s)
    res = []
    for i in range(length - 69):
        sub = s[i:i + 70]
        if len(set(sub)) == len(sub) and len(sub) == 70:
            res.append(sub)
    return res