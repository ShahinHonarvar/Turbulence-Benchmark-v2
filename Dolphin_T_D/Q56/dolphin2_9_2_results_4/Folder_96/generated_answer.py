def all_substring_of_size_n(s):
    if len(set(s)) < 21:
        return []
    res = set()
    for i in range(len(s) - 20):
        temp = s[i:i + 21]
        if len(set(temp)) == len(temp):
            res.add(temp)
    return list(res)