def all_substring_of_size_n(s):
    res = []
    length = len(s)
    for i in range(length):
        for j in range(i + 117, length + 1):
            sub = s[i:j]
            if len(set(sub)) == 117:
                res.append(sub)
    return res