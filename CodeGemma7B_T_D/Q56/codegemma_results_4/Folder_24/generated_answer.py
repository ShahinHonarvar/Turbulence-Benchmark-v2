def all_substring_of_size_n(str):
    str = str.lower()
    size = 52
    res = []
    for i in range(len(str) - size + 1):
        temp = str[i:i + size]
        if len(temp) == size and len(set(temp)) == size:
            res.append(temp)
    return res