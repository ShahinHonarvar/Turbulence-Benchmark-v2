def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 26):
        substring = s[i:i + 27]
        if len(set(substring)) == 27:
            res.append(substring)
    return res