def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 89):
        substring = s[i:i + 90]
        if len(set(substring)) == 90:
            res.append(substring)
    return res