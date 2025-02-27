def all_substring_of_size_n(s):
    n = 77
    res = []
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            substr = s[i:j]
            if len(set(substr)) == n:
                res.append(substr)
    return res