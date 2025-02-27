def all_substring_of_size_n(str):
    res = set()
    for i in range(len(str)):
        for j in range(i + 1, len(str)):
            if len(set(str[i:j + 1])) == 32:
                res.add(str[i:j + 1])
    return list(res)