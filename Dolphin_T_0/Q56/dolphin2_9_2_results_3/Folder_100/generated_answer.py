def all_substring_of_size_n(s):
    res = []
    for i in range(len(s)):
        if len(set(s[i:i + 92])) == 92:
            res.append(s[i:i + 92])
    return list(set(res))