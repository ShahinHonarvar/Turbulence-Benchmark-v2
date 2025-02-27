def all_substring_of_size_n(text):
    res = set()
    for i in range(len(text) - 55 + 1):
        res.add(text[i:i + 55])
    return list(res)