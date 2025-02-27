def all_substring_of_size_n(s):
    n = 130
    if len(s) < n:
        return []
    subs = []
    for i in range(len(s) - n + 1):
        if len(set(s[i:i + n])) == n:
            subs.append(s[i:i + n])
    return subs