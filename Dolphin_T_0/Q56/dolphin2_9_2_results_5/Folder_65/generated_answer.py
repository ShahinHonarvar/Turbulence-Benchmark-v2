def all_substring_of_size_n(s):
    subs = set()
    n = len(s)
    for i in range(n - 79):
        sub = s[i:i + 80]
        if len(set(sub)) == 80:
            subs.add(sub)
    return list(subs)