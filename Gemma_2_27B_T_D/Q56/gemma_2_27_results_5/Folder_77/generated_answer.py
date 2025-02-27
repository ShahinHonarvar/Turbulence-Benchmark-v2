def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 143):
        substring = s[i:i + 144]
        if len(set(substring)) == 144:
            res.append(substring)
    return res