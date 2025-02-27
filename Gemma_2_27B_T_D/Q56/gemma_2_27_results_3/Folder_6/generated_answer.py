def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 22):
        substring = s[i:i + 23]
        if len(set(substring)) == 23:
            res.append(substring)
    return res