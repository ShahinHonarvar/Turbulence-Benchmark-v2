def all_substring_of_size_n(text):
    res = set()
    for i in range(len(text) - 96):
        res.add(text[i:i + 97])
    return list(res)