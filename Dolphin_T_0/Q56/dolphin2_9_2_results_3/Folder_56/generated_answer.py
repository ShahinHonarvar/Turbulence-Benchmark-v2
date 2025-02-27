def all_substring_of_size_n(s):
    n = 69
    res = set()
    for i in range(len(s) - n + 1):
        temp = s[i:i + n]
        if len(set(temp)) == n:
            res.add(temp)
    return list(res)