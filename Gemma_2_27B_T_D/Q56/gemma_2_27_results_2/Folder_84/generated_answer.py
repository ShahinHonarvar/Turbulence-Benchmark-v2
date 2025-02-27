def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 113):
        substring = s[i:i + 114]
        if len(set(substring)) == 114:
            res.append(substring)
    return res