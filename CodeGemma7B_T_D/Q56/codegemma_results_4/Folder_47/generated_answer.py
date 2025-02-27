def all_substring_of_size_n(text):
    res = set()
    for i in range(len(text) - 91 + 1):
        res.add(text[i:i + 91])
    return list(res)