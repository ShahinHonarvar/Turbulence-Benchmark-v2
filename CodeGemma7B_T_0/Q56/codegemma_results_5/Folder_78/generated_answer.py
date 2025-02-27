def all_substring_of_size_n(str):
    res = set()
    for i in range(len(str)):
        for j in range(i + 49, len(str) + 1):
            res.add(str[i:j])
    return list(res)