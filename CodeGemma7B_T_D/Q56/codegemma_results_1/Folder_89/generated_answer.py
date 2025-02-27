def all_substring_of_size_n(txt):
    res = []
    for i in range(len(txt) - n + 1):
        check_set = set(txt[i:i + n])
        if len(check_set) == n:
            res.append(txt[i:i + n])
    return res