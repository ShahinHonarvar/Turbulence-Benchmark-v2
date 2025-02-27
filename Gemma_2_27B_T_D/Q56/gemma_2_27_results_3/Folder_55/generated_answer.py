def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 39):
        substring = s[i:i + 40]
        if len(set(substring)) == 40:
            res.append(substring)
    return res