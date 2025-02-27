def all_substring_of_size_n(s):
    res = []
    n = len(s)
    for i in range(n - 90):
        substring = s[i:i + 91]
        if len(set(substring)) == 91:
            res.append(substring)
    return res