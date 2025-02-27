def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 69):
        substring = s[i:i + 70]
        if len(set(substring)) == 70:
            res.append(substring)
    return res