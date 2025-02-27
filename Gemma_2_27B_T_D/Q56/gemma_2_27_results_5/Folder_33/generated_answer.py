def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 104):
        substring = s[i:i + 105]
        if len(set(substring)) == 105:
            res.append(substring)
    return res