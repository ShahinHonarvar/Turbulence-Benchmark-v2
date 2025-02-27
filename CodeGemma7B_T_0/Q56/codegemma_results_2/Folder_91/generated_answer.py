def all_substring_of_size_n(text):
    res = set()
    for i in range(len(text) - 5):
        res.add(text[i:i + 6])
    return list(res)