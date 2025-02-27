def all_substring_of_size_n(s):
    if len(s) < 10:
        return []
    res = []
    for i in range(len(s) - 9):
        substring = s[i:i + 10]
        if substring not in res:
            res.append(substring)
    return res