def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 145):
        if len(set(s[i:i + 146])) == 146:
            res.append(s[i:i + 146])
    return res