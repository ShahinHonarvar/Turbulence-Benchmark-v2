def all_substring_of_size_n(s):
    if len(s) < 17:
        return []
    subs = set()
    for i in range(len(s) - 17 + 1):
        sub = s[i:i + 17]
        if len(set(sub)) == 17:
            subs.add(sub)
    return list(subs)