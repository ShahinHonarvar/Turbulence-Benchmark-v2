def all_substring_of_size_n(s):
    if len(set(s)) < 98:
        return []
    res = set()
    for i in range(len(s) - 97):
        temp = s[i:i + 98]
        if len(set(temp)) == len(temp):
            res.add(temp)
    return list(res)