def all_substring_of_size_n(text):
    res = set()
    for i in range(len(text) - 95 + 1):
        res.add(text[i:i + 95])
    return list(res)