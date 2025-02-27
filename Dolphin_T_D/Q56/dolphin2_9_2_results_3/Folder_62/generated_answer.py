def all_substring_of_size_n(s):
    if len(s) < 32:
        return []
    subs = set()
    for i in range(len(s) - 31):
        if len(set(s[i:i + 32])) == 32:
            subs.add(s[i:i + 32])
    return list(subs)