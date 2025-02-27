def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 34 + 1):
        substring = s[i:i + 34]
        if len(set(substring)) == 34:
            res.append(substring)
    return res