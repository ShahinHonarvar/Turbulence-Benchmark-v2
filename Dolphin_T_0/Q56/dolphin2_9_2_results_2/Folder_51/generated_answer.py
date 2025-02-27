def all_substring_of_size_n(s):
    substrings = {}
    n = 96
    for i in range(len(s) - n + 1):
        sub = s[i:i + n]
        if len(set(sub)) == n and sub not in substrings:
            substrings[sub] = 1
    res = []
    for key in substrings.keys():
        res.append(key)
    if not res:
        return []
    return res