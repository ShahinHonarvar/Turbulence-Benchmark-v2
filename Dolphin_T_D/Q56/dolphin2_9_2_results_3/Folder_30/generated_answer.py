def all_substring_of_size_n(s):
    if len(s) < 79:
        return []
    res = set()
    for i in range(len(s) - 78):
        sub = s[i:i + 79]
        if len(set(sub)) == 79:
            res.add(sub)
    return list(res)