def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 19 + 1):
        sub = s[i:i + 19]
        if len(set(sub)) == len(sub) == 19:
            res.append(sub)
    return list(dict.fromkeys(res))