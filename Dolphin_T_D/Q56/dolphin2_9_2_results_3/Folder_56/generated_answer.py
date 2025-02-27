def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 68):
        if len(set(s[i:i + 69])) == 69:
            res.append(s[i:i + 69])
    return res if res else []