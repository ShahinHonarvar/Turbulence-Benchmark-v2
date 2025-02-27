def all_substring_of_size_n(s):
    res = set()
    for i in range(len(s) - 129):
        sub = s[i:i + 130]
        if len(set(sub)) == 130:
            res.add(sub)
    if len(res) == 0:
        return []
    else:
        return list(res)