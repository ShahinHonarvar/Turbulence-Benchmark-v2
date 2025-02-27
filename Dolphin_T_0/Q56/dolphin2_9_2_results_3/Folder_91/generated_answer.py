def all_substring_of_size_n(s):
    if len(s) < 6:
        return []
    subs = set()
    for i in range(len(s) - 5):
        sub = s[i:i + 6]
        if len(set(sub)) == len(sub):
            subs.add(sub)
    return list(subs)