def all_substring_of_size_n(s):
    n = len(s)
    subs = set()
    for i in range(n - 24):
        sub = s[i:i + 25]
        if len(set(sub)) == 25:
            subs.add(sub)
    return list(subs)