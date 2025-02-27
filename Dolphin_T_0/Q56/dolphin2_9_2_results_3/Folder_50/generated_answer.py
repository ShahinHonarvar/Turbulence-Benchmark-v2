def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 11 + 1):
        subs = s[i:i + 11]
        if len(set(subs)) == 11:
            res.append(subs)
    return res