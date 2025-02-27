def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 129):
        sub = s[i:i + 130]
        if len(set(sub)) == 130:
            res.append(sub)
    return res