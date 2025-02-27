def all_substring_of_size_n(str):
    res = set()
    for i in range(len(str) - 59):
        res.add(str[i:i + 60])
    return list(res)