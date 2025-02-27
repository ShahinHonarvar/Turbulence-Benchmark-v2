def all_substring_of_size_n(s):
    if len(s) < 8:
        return []
    n = len(s)
    sub = set()
    for i in range(n - 7):
        if len(set(s[i:i + 8])) == 8:
            sub.add(s[i:i + 8])
    return list(sub)