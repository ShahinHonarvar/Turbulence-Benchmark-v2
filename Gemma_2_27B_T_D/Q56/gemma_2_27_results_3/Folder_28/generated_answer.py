def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 43):
        substring = s[i:i + 44]
        if len(set(substring)) == 44:
            res.append(substring)
    return res