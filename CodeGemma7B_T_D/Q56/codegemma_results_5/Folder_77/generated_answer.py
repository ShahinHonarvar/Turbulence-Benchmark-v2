def all_substring_of_size_n(s):
    res = set()
    for i in range(len(s) - 143):
        res.add(s[i:i + 144])
    if not res:
        return []
    else:
        return list(res)