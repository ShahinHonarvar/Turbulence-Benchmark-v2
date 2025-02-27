def all_substring_of_size_n(str):
    res = set()
    for i in range(len(str) - 64):
        res.add(str[i:i + 65])
    return list(res)