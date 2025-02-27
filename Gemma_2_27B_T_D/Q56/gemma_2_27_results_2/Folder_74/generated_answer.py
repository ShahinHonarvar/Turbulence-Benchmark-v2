def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 96):
        substring = s[i:i + 97]
        if len(set(substring)) == 97:
            res.append(substring)
    return res