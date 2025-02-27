def all_substring_of_size_n(str1):
    n = 73
    res = set()
    for i in range(0, len(str1)):
        sub = str1[i:i + n]
        if len(sub) == n and len(set(sub)) == n:
            res.add(sub)
    return list(res)