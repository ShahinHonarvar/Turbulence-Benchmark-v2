def all_substring_of_size_n(s):
    if len(s) < 81:
        return []
    subs = set()
    for i in range(len(s) - 80):
        sub = s[i:i + 81]
        if len(set(sub)) == 81:
            subs.add(sub)
    return list(subs)