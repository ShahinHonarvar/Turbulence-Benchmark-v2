def all_substring_of_size_n(text):
    res = set()
    for i in range(len(text) - 73):
        res.add(text[i:i + 74])
    return list(res)