def all_substring_of_size_n(str):
    res = []
    for i in range(len(str)):
        for j in range(i + 96, len(str) + 1):
            tmp = str[i:j]
            if len(tmp) == 96 and len(set(tmp)) == 96:
                res.append(tmp)
    return list(set(res))