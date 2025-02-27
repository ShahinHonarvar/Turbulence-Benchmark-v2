def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 123):
        sub = s[i:i + 124]
        if len(set(sub)) == 124:
            res.append(sub)
    return res