def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 20):
        substring = s[i:i + 21]
        if len(set(substring)) == 21:
            res.append(substring)
    return res