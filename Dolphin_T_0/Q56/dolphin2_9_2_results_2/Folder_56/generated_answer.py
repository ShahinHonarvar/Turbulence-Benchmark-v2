def all_substring_of_size_n(s):
    n = 69
    if len(set(s)) != n:
        return []
    else:
        subs = set()
        for i in range(len(s) - n + 1):
            subs.add(s[i:i + n])
        return list(subs)