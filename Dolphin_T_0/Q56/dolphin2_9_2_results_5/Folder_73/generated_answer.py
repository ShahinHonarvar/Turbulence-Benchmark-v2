def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 19):
        temp = s[i:i + 20]
        if len(set(temp)) == len(temp):
            res.append(temp)
    return res