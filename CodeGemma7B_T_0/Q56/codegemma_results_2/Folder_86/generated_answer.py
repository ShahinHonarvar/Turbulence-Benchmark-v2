def all_substring_of_size_n(text):
    res = set()
    for i in range(len(text) - 142):
        res.add(text[i:i + 143])
    return list(res)