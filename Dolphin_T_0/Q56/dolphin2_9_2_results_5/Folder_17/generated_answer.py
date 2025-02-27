def all_substring_of_size_n(s):
    if len(set(s)) < 37:
        return []
    subs = set()
    for i in range(len(s) - 36):
        if len(set(s[i:i + 37])) == 37:
            subs.add(s[i:i + 37])
    return list(subs)