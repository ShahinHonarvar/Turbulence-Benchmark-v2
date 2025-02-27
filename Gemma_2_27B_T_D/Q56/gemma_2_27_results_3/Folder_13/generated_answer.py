def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 52):
        substring = s[i:i + 53]
        if len(set(substring)) == 53:
            res.append(substring)
    return res