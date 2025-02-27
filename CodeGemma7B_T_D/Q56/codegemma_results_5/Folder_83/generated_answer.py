def all_substring_of_size_n(s):
    res = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            tmp = s[i:j]
            if len(tmp) == 48 and len(tmp) == len(set(tmp)):
                res.add(tmp)
    return list(res)