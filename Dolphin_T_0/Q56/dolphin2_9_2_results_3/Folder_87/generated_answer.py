def all_substring_of_size_n(s):
    if len(s) < 58:
        return []
    subs = set()
    for i in range(len(s) - 57):
        sub = s[i:i + 58]
        if len(set(sub)) == 58:
            subs.add(sub)
    return list(subs)