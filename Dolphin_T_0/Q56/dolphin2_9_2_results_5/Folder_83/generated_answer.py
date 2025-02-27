def all_substring_of_size_n(s):
    n = 48
    subs = set()
    for i in range(len(s) - n + 1):
        subs.add(s[i:i + n])
    if n > len(set(s)):
        return []
    res = []
    for sub in subs:
        if len(set(sub)) == n:
            res.append(sub)
    return res