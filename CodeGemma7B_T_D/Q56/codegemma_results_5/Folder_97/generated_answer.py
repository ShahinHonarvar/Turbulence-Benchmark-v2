def all_substring_of_size_n(s):
    res = set()
    for i in range(len(s) - 142 + 1):
        for j in range(i + 20, len(s) - 122 + 1):
            if len(set(s[i:j])) == 142:
                res.add(s[i:j])
    return list(res) if res else []