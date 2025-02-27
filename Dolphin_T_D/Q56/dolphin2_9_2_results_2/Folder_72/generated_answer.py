def all_substring_of_size_n(s):
    if len(s) < 88:
        return []
    subs = set()
    for i in range(len(s) - 87):
        if len(set(s[i:i + 88])) == 88:
            subs.add(s[i:i + 88])
    return list(subs)