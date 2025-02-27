def all_substring_of_size_n(s):
    res = []
    for i in range(len(s)):
        for j in range(i + 34, len(s) + 1):
            sub = s[i:j]
            if len(set(sub)) == 34:
                res.append(sub)
    return res