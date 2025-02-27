def all_substring_of_size_n(s):
    if len(s) < 110:
        return []
    subs = set()
    for i in range(len(s) - 110 + 1):
        sub = s[i:i + 110]
        if len(sub) == len(set(sub)):
            subs.add(sub)
    return list(subs)