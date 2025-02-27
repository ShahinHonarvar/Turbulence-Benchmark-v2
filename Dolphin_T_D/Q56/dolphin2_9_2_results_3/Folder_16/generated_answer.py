def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 123):
        subs = s[i:i + 124]
        if len(set(subs)) == 124:
            res.append(subs)
    return res