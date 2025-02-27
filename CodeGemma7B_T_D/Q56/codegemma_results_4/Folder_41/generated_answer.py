def all_substring_of_size_n(s):
    d = set()
    for i in range(len(s) - 74 + 1):
        d.add(s[i:i + 74])
    return list(d)