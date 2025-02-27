def all_substring_of_size_n(s):
    subs = set()
    n = len(s)
    for i in range(n):
        for j in range(i + 11, n + 1):
            if len(set(s[i:j])) == 11:
                subs.add(s[i:j])
    return list(subs)