def all_substring_of_size_n(s):
    n = len(s)
    subs = set()
    for i in range(n - 42):
        sub = s[i:i + 43]
        if len(set(sub)) == 43:
            subs.add(sub)
    return list(subs)