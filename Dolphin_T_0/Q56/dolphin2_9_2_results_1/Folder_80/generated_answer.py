def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 2):
        if len(set(s[i:i + 31])) == 31:
            res.append(s[i:i + 31])
    return list(set(res))