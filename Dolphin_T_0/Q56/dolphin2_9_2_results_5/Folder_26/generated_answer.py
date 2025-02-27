def all_substring_of_size_n(s):
    res = []
    if len(set(s)) != len(s) or len(s) < 33:
        return res
    else:
        for i in range(len(s) - 32):
            if len(set(s[i:i + 33])) == 33:
                res.append(s[i:i + 33])
    return list(set(res))