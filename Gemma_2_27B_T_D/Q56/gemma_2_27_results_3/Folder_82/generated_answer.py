def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 99):
        substring = s[i:i + 100]
        if len(set(substring)) == 100:
            res.append(substring)
    return res