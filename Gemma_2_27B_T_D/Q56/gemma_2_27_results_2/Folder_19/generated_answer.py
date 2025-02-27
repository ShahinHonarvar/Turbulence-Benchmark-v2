def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 17):
        substring = s[i:i + 18]
        if len(set(substring)) == 18:
            res.append(substring)
    return res