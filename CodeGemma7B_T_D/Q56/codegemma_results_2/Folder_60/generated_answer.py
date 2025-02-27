def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 36 + 1):
        if len(set(s[i:i + 36])) == 36:
            res.append(s[i:i + 36])
    return res