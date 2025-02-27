def all_substring_of_size_n(s):
    n = len(s)
    subs = []
    for i in range(n - 7):
        sub = s[i:i + 8]
        if len(set(sub)) == 8 and sub not in subs:
            subs.append(sub)
    return subs