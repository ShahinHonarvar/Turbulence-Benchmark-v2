def all_substring_of_size_n(s):
    if len(s) < 65:
        return []
    subs = set()
    for i in range(len(s) - 64):
        sub = s[i:i + 65]
        if len(set(sub)) == 65:
            subs.add(sub)
    return list(subs)