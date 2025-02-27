def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 51):
        substring = s[i:i + 52]
        if len(set(substring)) == 52:
            res.append(substring)
    return res