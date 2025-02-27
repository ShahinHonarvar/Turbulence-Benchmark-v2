def all_substring_of_size_n(word):
    res = set()
    for i in range(len(word) - 94 + 1):
        res.add(word[i:i + 94])
    return list(res)