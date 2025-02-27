def all_substring_of_size_n(s):
    res = []
    if len(set(s)) < 61:
        return res
    for i in range(len(s) - 60):
        temp = s[i:i + 61]
        if len(set(temp)) == 61:
            res.append(temp)
    return res