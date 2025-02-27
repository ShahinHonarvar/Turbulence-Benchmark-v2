def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 119):
        substring = s[i:i + 120]
        if len(set(substring)) == 120:
            res.append(substring)
    return res