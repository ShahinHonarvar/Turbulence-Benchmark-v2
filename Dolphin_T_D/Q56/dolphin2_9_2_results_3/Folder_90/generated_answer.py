def all_substring_of_size_n(s):
    if len(set(s)) < 130:
        return []
    subs = set()
    for i in range(len(s) - 130 + 1):
        subs.add(s[i:i + 130])
    return list(subs)