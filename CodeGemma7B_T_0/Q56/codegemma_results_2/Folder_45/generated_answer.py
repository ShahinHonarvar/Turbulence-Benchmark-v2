def all_substring_of_size_n(text):
    res = set()
    for i in range(len(text) - 28):
        res.add(text[i:i + 29])
    return list(res)