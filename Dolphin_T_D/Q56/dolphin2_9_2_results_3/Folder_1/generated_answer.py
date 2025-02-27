def all_substring_of_size_n(s):
    n = 24
    subs = set()
    for i in range(len(s) - n + 1):
        if len(set(s[i:i + n])) == n:
            subs.add(s[i:i + n])
    return list(subs)