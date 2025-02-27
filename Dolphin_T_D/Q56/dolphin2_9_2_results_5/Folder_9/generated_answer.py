def all_substring_of_size_n(s):
    subs = set()
    n = len(s)
    for i in range(n):
        for j in range(i + 34, n + 1):
            sub = s[i:j]
            if len(set(sub)) == len(sub):
                subs.add(sub)
    return list(subs)