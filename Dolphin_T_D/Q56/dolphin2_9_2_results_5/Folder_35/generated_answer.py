def all_substring_of_size_n(s):
    if len(s) < 27:
        return []
    res = set()
    for i in range(len(s) - 26):
        sub = s[i:i + 27]
        if len(set(sub)) == 27:
            res.add(sub)
    return list(res)