def all_substring_of_size_n(s):
    n = len(s)
    subs = []
    for i in range(n - 38):
        sub = s[i:i + 39]
        if len(set(sub)) == 39:
            subs.append(sub)
    return subs