def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 64):
        substring = s[i:i + 65]
        if len(set(substring)) == 65:
            res.append(substring)
    return res