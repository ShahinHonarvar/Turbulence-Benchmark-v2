def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 37):
        substring = s[i:i + 38]
        if len(set(substring)) == 38:
            res.append(substring)
    return res