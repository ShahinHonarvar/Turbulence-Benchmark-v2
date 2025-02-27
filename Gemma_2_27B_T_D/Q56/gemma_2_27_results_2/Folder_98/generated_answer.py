def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 9):
        substring = s[i:i + 10]
        if len(set(substring)) == 10:
            res.append(substring)
    return res