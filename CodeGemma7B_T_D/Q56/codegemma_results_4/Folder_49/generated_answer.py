def all_substring_of_size_n(s):
    res = set()
    for i in range(len(s) - 72):
        res.add(s[i:i + 73])
    return list(res) if res else []