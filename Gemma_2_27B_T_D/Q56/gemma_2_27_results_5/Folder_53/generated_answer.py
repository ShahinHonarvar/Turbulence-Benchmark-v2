def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 24):
        substring = s[i:i + 25]
        if len(set(substring)) == 25:
            res.append(substring)
    return res