def all_substring_of_size_n(s):
    subs = set()
    n = len(s)
    for i in range(n - 2):
        sub = s[i:i + 3]
        if len(set(sub)) == 3:
            subs.add(sub)
    return list(subs)