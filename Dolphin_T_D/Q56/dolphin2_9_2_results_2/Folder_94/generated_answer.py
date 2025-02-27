def all_substring_of_size_n(s):
    n = 70
    subs = set()
    if len(s) < n:
        return []
    else:
        for i in range(len(s) - n + 1):
            sub = s[i:i + n]
            if len(set(sub)) == n:
                subs.add(sub)
    return list(subs)