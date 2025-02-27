def all_substring_of_size_n(s):
    res = []
    n = 93
    if len(s) < n:
        return res
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == n:
            res.append(substring)
    return res