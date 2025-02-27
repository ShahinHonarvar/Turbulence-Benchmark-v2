def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 31):
        substring = s[i:i + 32]
        if len(set(substring)) == 32:
            res.append(substring)
    return res