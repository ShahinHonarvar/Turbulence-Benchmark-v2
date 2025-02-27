def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 62):
        substring = s[i:i + 63]
        if len(set(substring)) == 63:
            res.append(substring)
    return res