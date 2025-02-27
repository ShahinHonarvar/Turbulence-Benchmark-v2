def all_substring_of_size_n(text):
    res = set()
    for i in range(len(text)):
        for j in range(i + 20, len(text) + 1):
            res.add(text[i:j])
    return list(res)