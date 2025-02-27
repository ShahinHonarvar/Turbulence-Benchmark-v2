def all_substring_of_size_n(s):
    if len(set(s)) < 43:
        return []
    subs = set()
    for i in range(len(s) - 42):
        subs.add(s[i:i + 43])
    return list(subs)