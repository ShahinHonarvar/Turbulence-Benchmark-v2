def all_substring_of_size_n(s):
    if len(s) < 74:
        return []
    a = [s[i:i + 74] for i in range(len(s) - 73)]
    res = []
    for i in a:
        if len(set(i)) == 74:
            res.append(i)
    return res