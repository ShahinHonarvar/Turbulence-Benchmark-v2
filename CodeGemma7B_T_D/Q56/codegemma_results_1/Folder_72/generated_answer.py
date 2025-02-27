def all_substring_of_size_n(str):
    res = set()
    for i in range(len(str) - 87):
        res.add(str[i:i + 88])
    return list(res)