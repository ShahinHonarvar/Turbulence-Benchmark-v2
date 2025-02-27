def all_substring_of_size_n(text):
    res = set()
    for i in range(len(text) - 22):
        res.add(text[i:i + 23])
    return list(res)