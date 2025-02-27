def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 44):
        substring = s[i:i + 45]
        if len(set(substring)) == 45:
            res.append(substring)
    return res