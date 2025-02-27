def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 28):
        substring = s[i:i + 29]
        if len(set(substring)) == 29:
            res.append(substring)
    return res