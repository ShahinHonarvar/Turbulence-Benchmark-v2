def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 19):
        substring = s[i:i + 20]
        if len(set(substring)) == 20:
            res.append(substring)
    return res