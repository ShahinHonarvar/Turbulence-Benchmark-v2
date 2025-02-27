def all_substring_of_size_n(s):
    subs = set()
    n = len(s)
    for i in range(n - 23):
        sub = s[i:i + 24]
        if len(set(sub)) == 24:
            subs.add(sub)
    return list(subs)