def all_substring_of_size_n(s):
    str_size = 79
    res = set()
    for i in range(len(s) - str_size + 1):
        sub = s[i:i + str_size]
        if len(set(sub)) == str_size:
            res.add(sub)
    return list(res)