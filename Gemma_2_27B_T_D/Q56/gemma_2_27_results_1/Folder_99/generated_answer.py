def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 109):
        substring = s[i:i + 110]
        if len(set(substring)) == 110:
            res.append(substring)
    return res