def all_substring_of_size_n(text):
    res = set()
    for i in range(len(text) - 45):
        res.add(text[i:i + 46])
    return list(res)