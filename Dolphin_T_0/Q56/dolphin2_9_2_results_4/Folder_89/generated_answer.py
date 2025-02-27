def all_substring_of_size_n(s):
    if len(s) < 38:
        return []
    sub = set()
    for i in range(len(s) - 37):
        if len(set(s[i:i + 38])) == 38:
            sub.add(s[i:i + 38])
    return list(sub)