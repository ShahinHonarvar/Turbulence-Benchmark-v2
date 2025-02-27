def all_substring_of_size_n(str1):
    if len(str1) < 149:
        return []
    res = set()
    for i in range(len(str1) - 148):
        res.add(str1[i:i + 149])
    return list(res)