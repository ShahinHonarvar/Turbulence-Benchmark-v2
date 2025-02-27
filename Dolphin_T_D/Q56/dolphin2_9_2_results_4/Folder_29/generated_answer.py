def all_substring_of_size_n(s):
    if len(set(s)) != 95:
        return []
    subs = set()
    for i in range(len(s) - 94):
        subs.add(s[i:i + 95])
    return list(subs)