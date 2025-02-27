def all_substring_of_size_n(s):
    res = []
    n = len(s)
    for i in range(n - 89):
        if len(set(s[i:i + 90])) == 90:
            res.append(s[i:i + 90])
    return res