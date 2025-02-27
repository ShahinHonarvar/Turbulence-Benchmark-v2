def all_substring_of_size_n(string):
    if len(string) < 28:
        return []
    res = []
    for i in range(len(string) - 27):
        subset = string[i:i + 28]
        if len(set(list(subset))) == 28:
            res.append(subset)
    return res