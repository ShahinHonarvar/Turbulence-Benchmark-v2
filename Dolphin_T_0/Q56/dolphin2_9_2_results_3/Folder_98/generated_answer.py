def all_substring_of_size_n(s):
    subs = set()
    n = 10
    for i in range(len(s) - n + 1):
        sub = s[i:i + n]
        if len(set(sub)) == n:
            subs.add(sub)
    return list(subs)