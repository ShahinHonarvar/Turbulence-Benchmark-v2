def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 84):
        substring = s[i:i + 85]
        if len(set(substring)) == 85:
            res.append(substring)
    return res