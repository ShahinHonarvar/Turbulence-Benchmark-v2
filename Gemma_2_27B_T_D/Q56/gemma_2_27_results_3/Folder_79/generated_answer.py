def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 60):
        substring = s[i:i + 61]
        if len(set(substring)) == 61:
            res.append(substring)
    return res