def all_substring_of_size_n(s):
    if len(s) < 29:
        return []
    subs = set()
    for i in range(len(s) - 28):
        sub = s[i:i + 29]
        if len(set(sub)) == 29:
            subs.add(sub)
    return list(subs)