def all_substring_of_size_n(s):
    n = 42
    res = []
    for i in range(len(s) - n + 1):
        sub_str = s[i:i + n]
        if len(set(sub_str)) == n:
            res.append(sub_str)
    return res