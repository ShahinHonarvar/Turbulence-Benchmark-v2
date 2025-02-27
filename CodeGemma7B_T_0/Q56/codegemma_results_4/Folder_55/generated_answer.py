def all_substring_of_size_n(text):
    res = set()
    for i in range(len(text) - 39):
        res.add(text[i:i + 40])
    return list(res)