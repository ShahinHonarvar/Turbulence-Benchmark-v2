def all_substring_of_size_n(text):
    n = 42
    res = set()
    for i in range(len(text)):
        for j in range(i + n, len(text) + 1):
            substring = text[i:j]
            res.add(substring)
    if len(res) == 0:
        return []
    else:
        return list(res)