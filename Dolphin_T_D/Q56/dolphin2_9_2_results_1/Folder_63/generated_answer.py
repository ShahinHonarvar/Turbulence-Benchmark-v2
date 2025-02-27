def all_substring_of_size_n(s):
    if len(s) < 19:
        return []
    subs = set()
    for i in range(0, len(s) - 19 + 1):
        if len(set(s[i:i + 19])) == 19:
            subs.add(s[i:i + 19])
    return list(subs)